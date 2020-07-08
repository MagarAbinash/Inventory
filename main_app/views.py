from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Supplier, Item, Category, SubCategory, Brand
from main_app import forms
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Abinash Rana'}
    return render(request, 'main_app/index.html', context=my_dict)

def dahsboard(request):
    item = Item.objects.all()
    brand = Brand.objects.all()
    supplier = Supplier.objects.all()
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    data_dict = {
        'item_table': item,
        'brand_table': brand,
        'supplier_table': supplier,
        'category_table': category,
        'subcat_table': subcat,
    }
    return render(request, 'main_app/dashboard.html', context=data_dict)


def supForm(request):
    form = forms.SupForm()

    if request.method == 'POST':
        form = forms.SupForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

        else:
            print("Error form invalid")

            
    return render(request, 'main_app/forms.html',{'form': form})

def catForm(request):
    form = forms.CatForm()

    if request.method == 'POST':
        form = forms.CatForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

        else:
            print("Error form invalid")

            
    return render(request, 'main_app/forms.html',{'form': form})

def subCatForm(request):
    form = forms.SubCatForm()

    if request.method == 'POST':
        form = forms.SubCatForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

        else:
            print("Error form invalid")

            
    return render(request, 'main_app/forms.html',{'form': form})

def brandForm(request):
    form = forms.BrandForm()

    if request.method == 'POST':
        form = forms.BrandForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

        else:
            print("Error form invalid")

            
    return render(request, 'main_app/forms.html',{'form': form})

def itemForm(request):
    form = forms.ItemForm()

    if request.method == 'POST':
        form = forms.ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)

        else:
            print("Error form invalid")

            
    return render(request, 'main_app/forms.html',{'form': form})

