from django import forms
from .models import  Product,Order

class productForm(forms.ModelForm):
	class Meta:
		model=Product
		fields = ['name','quantity','category']

class OrderForm(forms.ModelForm):
	class Meta:
		model=Order
		fields = ['product','order_quantity']