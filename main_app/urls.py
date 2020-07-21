from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/', views.userPage, name='userPage'),
    path('settings/', views.accountSettings, name='accountSettings'),

    path('purchase/', views.purchase, name='purchase'),
    path('sales/', views.sales, name='sales'),

    path('itemforms/', views.itemForm, name='itemForms'),
    path('updateItem/<str:pk>/', views.updateItem, name='updateItem'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='deleteItem'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]