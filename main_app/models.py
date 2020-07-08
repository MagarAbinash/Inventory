from django.db import models

# Create your models here.
class Supplier(models.Model):
    sup_name = models.CharField(max_length=50)
    sup_contact = models.CharField(max_length=10)
    sup_email = models.EmailField()

    def __str__(self):
        return self.sup_name

class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    cat_rel = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.subCat_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

    def __str__(self):
        return self.brand_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    brand_rel = models.ForeignKey(Brand, on_delete=models.CASCADE)
    cat_rel = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCat_rel = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    sup_rel = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name