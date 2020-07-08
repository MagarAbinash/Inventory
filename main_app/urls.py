from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dahsboard, name='dahsboard'),
    path('supforms/', views.supForm, name='supForms'),
    path('catforms/', views.catForm, name='catForms'),
    path('subcatforms/', views.subCatForm, name='subCatForms'),
    path('brandforms/', views.brandForm, name='brandForms'),
    path('itemforms/', views.itemForm, name='itemForms'),

]