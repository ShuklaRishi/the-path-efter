from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms

class SignUpForm(UserCreationForm):
	dob=forms.DateField()
	class Meta:
		model = MyUser
		fields="__all__"