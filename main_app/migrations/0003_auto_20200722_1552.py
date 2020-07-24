# Generated by Django 2.2.2 on 2020-07-22 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200722_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Category'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Category'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='subCat_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
