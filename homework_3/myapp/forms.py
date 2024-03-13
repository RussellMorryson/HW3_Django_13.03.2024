from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    description = forms.CharField(max_length=400)
    image = forms.ImageField(upload_to='products/')


    