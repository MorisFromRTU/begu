from django.db.models.signals import post_migrate
from django.core.files import File
from django.dispatch import receiver
from .models import Product, Category
from django.contrib.auth.models import User
import random

@receiver(post_migrate)
def create_default_products(sender, **kwargs):
    if sender.name == 'begu':
        if not Category.objects.exists():
            Category.objects.create(name='Nike', description='Description for Nike')
            Category.objects.create(name='New Balance', description='Description for New Balance')

        if not Product.objects.exists():
            category1 = Category.objects.get(name='Nike')
            category2 = Category.objects.get(name='New Balance')

            sizes = [str(size) for size in [36.0 + i * 0.5 for i in range(18)]]
            Product.objects.create(name='NIKE DUNK LOW RETRO PRM', 
                                   short_description='The iconic bright white Swoosh logo persists in cutting through the design.', 
                                   price=139.00, 
                                   category=category1,
                                   sizes = {size: random.randint(0, 10) for size in sizes},
                                   image = 'products/nike1.jpg'
                                   )
            Product.objects.create(name='NEW BALANCE U996GR', 
                                   short_description="Boston-based sneaker label New Balance's 996 ‘Made in USA’ sneaker makes a welcomed comeback this season", 
                                   price=219.00, 
                                   category=category2,
                                   sizes = {size: random.randint(0, 10) for size in sizes},
                                   image = 'products/nb1.jpg'
                                   )
            Product.objects.create(name='NEW BALANCE U996GR', 
                                   short_description="Boston-based sneaker label New Balance's 996 ‘Made in USA’ sneaker makes a welcomed comeback this season", 
                                   price=219.00, 
                                   category=category2,
                                   sizes = {size: random.randint(0, 10) for size in sizes},
                                   image = 'products/nb1.jpg'
                                   )
    if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'password')