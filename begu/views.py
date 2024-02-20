from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.core.exceptions import ValidationError

def main(request):
    return render(request, 'begu/main.html')

# def registration(request):
#     if request.method == 'POST':
#         login = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = User.objects.create(username=login, email=email, password=password)
#         new_customer = Customer(user=user)
#         new_customer.save()
#     return render(request, 'begu/registration.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  
    else:
        form = RegistrationForm()
    return render(request, 'begu/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        list(messages.get_messages(request))
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                print(user)
                
    else:
        form = LoginForm()

    return render(request, 'begu/login.html', {'form': form})