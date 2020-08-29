from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('user/', views.userPage, name='userPage'),
    path('settings/', views.accountSettings, name='accountSettings'),
    
    path('user_purchase/', views.customerPurchase, name='userPurchase'),
    path('user/purchase_details/<str:pk>/', views.purchaseDetails, name='purchaseDetails'),

    path('purchase/', views.purchase, name='purchase'),
    path('sales/', views.sales, name='sales'),

    path('itemforms/', views.itemForm, name='itemForms'),
    path('updateItem/<str:pk>/', views.updateItem, name='updateItem'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='deleteItem'),

    path('categoryforms/', views.createCategory, name='createCategory'),
    path('updateCategory/<str:pk>/', views.updateCategory, name='updateCategory'),
    path('deleteCategory/<str:pk>/', views.deleteCategory, name='deleteCategory'),

    path('subcategoryforms/', views.createSubCategory, name='createSubCategory'),
    path('updateSubCategory/<str:pk>/', views.updateSubCategory, name='updateSubCategory'),
    path('deleteSubCategory/<str:pk>/', views.deleteSubCategory, name='deleteSubCategory'),

    path('brandforms/', views.createBrand, name='createBrand'),
    path('updateBrand/<str:pk>/', views.updateBrand, name='updateBrand'),
    path('deleteBrand/<str:pk>/', views.deleteBrand, name='deleteBrand'),

    path('supplierforms/', views.createSupplier, name='createSupplier'),
    path('updateSupplier/<str:pk>/', views.updateSupplier, name='updateSupplier'),
    path('deleteSupplier/<str:pk>/', views.deleteSupplier, name='deleteSupplier'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]