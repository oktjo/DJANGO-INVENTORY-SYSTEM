from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUserForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		#fields = '__all__'
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	
	class Meta:
		model = User
		#fields = '__all__'
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		#fields = '__all__'
		fields = ['phone', 'address','image']