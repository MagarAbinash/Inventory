from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True, blank=True)
    profile_pic = models.ImageField(default='profile1.png', blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subCat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,  null=True, blank=True)
    quantity = models.DecimalField(default=0, max_digits=5, decimal_places=0)
    available = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

class Sales(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    def __str__(self):
        return str(self.item.name)

class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.item.name)
