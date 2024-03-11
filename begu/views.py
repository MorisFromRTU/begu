from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    return products

def category_list(request):
    categories = Category.objects.all()
    return categories

def all_sizes(request):
    sizes = [str(size) for size in [36.0 + i * 0.5 for i in range(18)]]
    return sizes

def main(request):
    products = product_list(request)
    categories = category_list(request)
    sizes = all_sizes(request)
    return render(request, 'begu/main.html', {'products': products, 'categories': categories, 'sizes': sizes})

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

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'begu/product_detail.html', {'product': product})

def apply_filters(request):
    if request.method == 'GET':
        brand = request.GET.getlist('brand')  
        size = request.GET.getlist('size')   
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        queryset = Product.objects.all()    

        if brand:
            brand_ids = [Category.objects.get(name=item).id for item in brand]
            queryset = queryset.filter(category__in=brand_ids)
            
        if size:
            for single_size in size:
                queryset = queryset.filter(sizes__contains=single_size)
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        categories = category_list(request)
        sizes = all_sizes(request)

        context = {
            'products': queryset,
            'categories': categories,
            'sizes': sizes
        }

        return render(request, 'begu/main.html', context)

    return render(request, 'begu/main.html')