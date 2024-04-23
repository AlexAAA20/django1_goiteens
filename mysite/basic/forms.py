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

class CreateFastForm(forms.Form):
	name = forms.CharField(label="Project Name")
	description = forms.CharField(label="Project Description")
	tags = forms.CharField(label="Add tags, separate by ,")
	url = forms.URLField(label="Project Link")