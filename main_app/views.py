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

# Admin Pages
@login_required(login_url='main_app:login')
@admin_only
def index(request):
    my_dict = {}
    return render(request, 'main_app/index.html', context=my_dict)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def dashboard(request):
    item = Item.objects.all()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    brand = Brand.objects.all()
    supplier = Supplier.objects.all()
    data_dict = {
        'item_table': item,
        'category_table': category,
        'subCategory_table': subcategory,
        'brand_table': brand,
        'supplier_table': supplier,
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
@allowed_user(allowed_roles=['Admin'])
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

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def createCategory(request):
    form = categoryForm()
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main_app/forms.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def updateCategory(request, pk):
    item = Category.objects.get(id=pk)
    form = categoryForm(instance=item)
    if request.method == "POST":
        form = categoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')
    
    return render(request, 'main_app/forms.html', {'form':form})

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def deleteCategory(request, pk):
    item = Category.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('main_app:dashboard')
    context = {'item': item, 'tableName': 'deleteItem'}
    return render(request, 'main_app/deleteItem.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def createSubCategory(request):
    form = subCategoryForm()
    if request.method == 'POST':
        form = subCategoryForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main_app/forms.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def updateSubCategory(request, pk):
    item = SubCategory.objects.get(id=pk)
    form = subCategoryForm(instance=item)
    if request.method == "POST":
        form = subCategoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')
    
    return render(request, 'main_app/forms.html', {'form':form})

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def deleteSubCategory(request, pk):
    item = SubCategory.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('main_app:dashboard')
    context = {'item': item, 'tableName': 'deleteItem'}
    return render(request, 'main_app/deleteItem.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def createSupplier(request):
    form = supplierForm()
    if request.method == 'POST':
        form = supplierForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main_app/forms.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def updateSupplier(request, pk):
    item = Supplier.objects.get(id=pk)
    form = supplierForm(instance=item)
    if request.method == "POST":
        form = supplierForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')
    
    return render(request, 'main_app/forms.html', {'form':form})

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def deleteSupplier(request, pk):
    item = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('main_app:dashboard')
    context = {'item': item, 'tableName': 'deleteItem'}
    return render(request, 'main_app/deleteItem.html', context)


@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def createBrand(request):
    form = brandForm()
    if request.method == 'POST':
        form = brandForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'main_app/forms.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def updateBrand(request, pk):
    item = Brand.objects.get(id=pk)
    form = brandForm(instance=item)
    if request.method == "POST":
        form = brandForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('main_app:dashboard')
    
    return render(request, 'main_app/forms.html', {'form':form})

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Admin'])
def deleteBrand(request, pk):
    item = Brand.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('main_app:dashboard')
    context = {'item': item, 'tableName': 'deleteItem'}
    return render(request, 'main_app/deleteItem.html', context)

# Login and Register Pages
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


# User Pages
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

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Customer'])
def customerPurchase(request):
    customer = request.user.customer
    form = SalesForm(initial={'customer': customer})
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data.get('item')
            qty = form.cleaned_data.get('quantity')
            if qty <= item.quantity:
                sales = form.save()
                print(sales)
                return redirect('main_app:userPage')

            else:
                messages.info(request, "Not enough item")

    context = {'form': form}
    return render(request, 'main_app/customer_purchase.html', context)

@login_required(login_url='main_app:login')
@allowed_user(allowed_roles=['Customer'])
def purchaseDetails(request,pk):
    purchase = Sales.objects.get(id=pk)
    context = {'item': purchase}
    return render(request, 'main_app/customer_purchase_details.html', context)