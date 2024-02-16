from django.shortcuts import render, redirect
from .models import User, Customer
from .forms import RegistrationForm

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
    else:
        #надо написать обработку ошибок
        form = RegistrationForm()
    return render(request, 'begu/registration.html', {'form': form})
