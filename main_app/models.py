from django.db import models

# Create your models here.
class Supplier(models.Model):
    sup_name = models.CharField(max_length=50)
    sup_contract = models.CharField(max_length=50)
    sup_address = models.TextField(max_length=200)
    sup_email = models.EmailField()

    def __str__(self):
        return self.sup_name

class Category(models.Model):
    cat_name = models.TextField(max_length=200)

    def __str__(self):
        return self.cat_name

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subCat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subCat_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    no_of_product = models.DecimalField(max_digits=5)
    amt = models.FloatField(max_length=8)

    def_str_(self):
        return item


