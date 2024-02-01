from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username = forms.CharField(label="Username", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'username', 'name': 'username', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'email', 'name': 'email', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'password1', 'name': 'password1', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label="Confirm Password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'password2', 'name': 'password2', 'placeholder': 'Enter Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class AccountForm(forms.Form):
    description = forms.CharField(label="Description", required=False, max_length=250, widget=forms.Textarea(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'description', 'name': 'descripción', 'placeholder': 'Enter Description'}))
    web_page = forms.CharField(label="Web Page", required=False, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'web_page', 'name': 'web_page', 'placeholder': 'Enter Web Page'}))
    avatar = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(
        attrs={'class': 'form-control bef bef-bg-darkolivegreen bef-text-honeydew', 'id': 'avatar', 'name': 'avatar', 'placeholder': 'Enter Avatar'}))
