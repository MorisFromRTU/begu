from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Product, Category

@receiver(post_migrate)
def create_default_products(sender, **kwargs):
    if sender.name == 'begu':
        if not Category.objects.exists():
            Category.objects.create(name='Nike', description='Description for Nike')
            Category.objects.create(name='New Balance', description='Description for New Balance')

        if not Product.objects.exists():
            category1 = Category.objects.get(name='Nike')
            category2 = Category.objects.get(name='New Balance')

            Product.objects.create(name='NIKE DUNK LOW RETRO PRM', short_description='The iconic bright white Swoosh logo persists in cutting through the design.', price=139.00, category=category1)
            Product.objects.create(name='NEW BALANCE U996GR', short_description="Boston-based sneaker label New Balance's 996 ‘Made in USA’ sneaker makes a welcomed comeback this season", price=219.00, category=category2)
