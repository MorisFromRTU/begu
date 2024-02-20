from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Customer

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label="Почта")
    username = forms.CharField(max_length=30, label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"]
        )
        customer = Customer.objects.create(user=user)
        return customer

class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
    
    error_messages = {
        'invalid_login': "Неверное имя пользователя или пароль.",
    }
