# Generated by Django 3.0.8 on 2020-07-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
