from django import forms
from django.contrib.auth.models import User
from .models import Customer

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label="Адрес электронной почты")
    username = forms.CharField(max_length=30, label="Никнейм")
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
        # Затем создаем клиента и связываем его с пользователем
        customer = Customer.objects.create(user=user)
        return customer
