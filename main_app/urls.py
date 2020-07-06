from django.urls import path
from main_app import views

urlpatterns = [
    path('dashboard/', views.dahsboard, name='dahsboard')
]