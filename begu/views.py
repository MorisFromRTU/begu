from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import Product, Category
from django.db.models import Q
from .utils import get_all_categories, get_all_sizes, get_product_list

def category_list(request):
    return get_all_categories()

def all_sizes(request):
    return get_all_sizes()

def product_list(request):
    return get_product_list()

def get_context_data(request, queryset):
    categories = category_list(request)
    sizes = all_sizes(request)
    context = {
        'products': queryset,
        'categories': categories,
        'sizes': sizes
    }
    return context

def main(request):
    products = product_list(request)
    context = get_context_data(request, products)
    return render(request, 'begu/main.html', context)

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
    queryset = Product.objects.all()
    
    if request.method == 'GET':
        brand = request.GET.getlist('brand')  
        size = request.GET.getlist('size')   
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        
        if brand:
            if brand != ["All Brands"]:
                brand_ids = [Category.objects.get(name=item).id for item in brand]
                queryset = queryset.filter(category__in=brand_ids)
            
        if size:
            if size != ["All Sizes"]:
                size_filter = Q()
                for single_size in size:
                    size_filter |= Q(**{"sizes__{}__gt".format(single_size): 0})
                queryset = queryset.filter(size_filter)
                    
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

    context = get_context_data(request, queryset)
    return render(request, 'begu/main.html', context)

def search_objects(request):
    queryset = product_list(request)

    if request.method == 'GET':
        search_text = request.GET.get('search_input').upper()
        
        if search_text:
            queryset = queryset.filter(name__icontains=search_text)
    
    context = get_context_data(request, queryset)
    return render(request, 'begu/main.html', context)
