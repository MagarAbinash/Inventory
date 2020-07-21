from .models import Customer, Item, Sales, Purchase
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance)
        print('Profile created')

post_save.connect(customer_profile, sender=User)

def sales_stock(sender, instance, created, **kwargs):
    if created:
        remaining_qty = instance.item.quantity - instance.quantity
        item = Item.objects.get(id=instance.item.id)
        item.quantity = remaining_qty
        item.save()

post_save.connect(sales_stock, sender=Sales)

def purchase_stock(sender, instance, created, **kwargs):
    if created:
        remaining_qty = instance.item.quantity + instance.quantity
        item = Item.objects.get(id=instance.item.id)
        item.quantity = remaining_qty
        item.save()

post_save.connect(purchase_stock, sender=Purchase)
