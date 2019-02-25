from django import forms
from products.models import Product, Category
from accounts.models import AccountUser

class UserCreateView(forms.ModelForm):
    class Meta:
        model = AccountUser
        fields = ['username', 'age', 'avatar']


class ProductCreateView(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'article', 'country', 'pakaging','figure', 'image','category_id']


class CategoryCreateView(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']