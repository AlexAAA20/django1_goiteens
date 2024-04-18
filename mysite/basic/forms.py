from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput())

class RegisterForm(forms.Form):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput())
	repeat_password = forms.CharField(label="Password (repeat it)", widget=forms.PasswordInput())

class TerminationForm(forms.Form):
	are_you_sure = forms.ChoiceField(choices=["Yes", "No"])
	security = forms.CharField(label="Password, just for security", widget=forms.PasswordInput())