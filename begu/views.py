from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Customer

def main(request):
    return render(request, 'begu/main.html')

def registration(request):
    if request.method == 'POST':
        login = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(username=login, email=email, password=password)
        new_customer = Customer(user=user)
        new_customer.save()
    return render(request, 'begu/registration.html')
