from django.contrib import admin
from main_app.models import Supplier, Brand, Category, SubCategory, Item
# Register your models here.


admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)

