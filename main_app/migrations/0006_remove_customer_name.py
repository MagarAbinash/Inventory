# Generated by Django 3.0.8 on 2020-07-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
