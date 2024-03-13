from .models import Product, Category

def get_all_categories():
    return Category.objects.all()

def get_all_sizes():
    return [str(size) for size in [36.0 + i * 0.5 for i in range(18)]]

def get_product_list():
    return Product.objects.all()
