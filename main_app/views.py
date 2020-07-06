from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Supplier, Item, Category, SubCategory, Brand
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Abinash Rana'}
    return render(request, 'main_app/index.html', context=my_dict)

def dahsboard(request):
    item = Item.objects.all()
    data_dict = {
        'item_table': item,
    }
    return render(request, 'main_app/dashboard.html', context=data_dict)