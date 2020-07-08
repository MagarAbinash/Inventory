from django import forms
from main_app.models import Supplier, Item, Category, SubCategory, Brand

class SupForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'

class CatForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class SubCatForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = '__all__'

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

