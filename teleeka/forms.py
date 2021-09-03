from django.forms import ModelForm

from django import forms 

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import *


# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username','email','password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateClientForm(ModelForm):
	class Meta:
		model = Client 
		fields = ['fullname', 'email','phone','group','status']
	
class CreateDepositForm(ModelForm):
	class Meta:
		model = Deposit 
		fields = '__all__'




class CreateWithdrawlForm(ModelForm):
	class Meta:
		model = Withdrawl 
		fields = '__all__'

class CreateSavingGroupForm(ModelForm):
	class Meta:
		model = SavingGroup 
		fields = '__all__'


