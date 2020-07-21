from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Customer
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
#Create your views here.

@login_required(login_url='main_app:login')
@admin_only
def index(request):
    my_dict = {'insert_me': 'Abinash Rana'}
    return render(request, 'main_app/index.html', context=my_dict)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def dashboard(request):
    item = Item.objects.all()
    data_dict = {
        'item_table': item,
    }
    return render(request, 'main_app/dashboard.html', context=data_dict)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def itemForm(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')

        else:
            print("Error form invalid")

            
    return render(request, 'main_app/forms.html',{'form': form})

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')
    
    return render(request, 'main_app/forms.html', {'form':form})

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('main_app:dashboard')
    context = {'item': item, 'tableName': 'deleteItem'}
    return render(request, 'main_app/deleteItem.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def purchase(request):
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')

    context = {'form': form}
    return render(request, 'main_app/forms.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin', 'Customer'])
def sales(request):
    form = SalesForm()
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data.get('item')
            qty = form.cleaned_data.get('quantity')
            print(item)
            if qty <= item.quantity:
                sales = form.save()
                return redirect('main_app:dashboard')

            else:
                messages.info(request, "Not enough item")

    context = {'form': form}
    return render(request, 'main_app/forms.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_app:index')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'main_app/login.html', context)

@unauthenticated_user
def registerPage(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Accounts was created for ' + username)
            return redirect('main_app:login')
        
    context = {'form': form}
    return render(request, 'main_app/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('main_app:login')


@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Customer'])
def userPage(request):
    purchase = request.user.customer.sales_set.all()
    context = {'purchase': purchase}
    return render(request, 'main_app/customer.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Customer'])
def accountSettings(request):
    user = request.user.customer
    form = CustomerForm(instance=user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'main_app/customer_settings.html', context)
