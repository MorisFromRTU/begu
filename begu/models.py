from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.postgres.fields import ArrayField

status_choices = [
    ('PENDING', 'Ожидает'),
    ('PROCESSING', 'Обработка'),
    ('SHIPPED', 'Отправлен'),
    ('DELIVERED', 'Доставлен'),
    ('CANCELLED', 'Отменён'),
    ]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    order_history = models.ManyToManyField('Order', blank=True)
    subscribed_to_newsletter = models.BooleanField(default=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sizes = models.JSONField(default=dict)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

