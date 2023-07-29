from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class" : "form-control text-placeholder ", 'placeholder': 'Введите E-mail:'}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control text-placeholder ", 'placeholder': 'Придумайте имя пользователя:'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control text-placeholder ", 'placeholder': 'Придумайте пароль:'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control text-placeholder ", 'placeholder': 'Придумайте пароль:'}))
    # spec = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control text-placeholder ", 'placeholder': 'Выберите специальность'}))
    spec = forms.ChoiceField(widget=forms.Select(attrs={"class" : "form-control text-placeholder ", 'placeholder': 'Выберите специальность'}), choices=(("Программист", "Программист"), ("Тестировщик", "Тестировщик"), ("Дизайнер", "Дизайнер")))

    class Meta:
        model = User
        fields = ['email', 'username',  'password1', 'password2', 'spec']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']