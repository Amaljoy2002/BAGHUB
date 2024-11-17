from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model  
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    # Add any additional fields you need
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Use email to log in instead of username
    REQUIRED_FIELDS = ['username']  # Username is still required to satisfy AbstractUser
    def __str__(self):
        return self.email  # Or self.username, but keep only one.

    
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Image field
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name




CustomUser = get_user_model()
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.product.price * self.quantity
    


from django.conf import settings
from django.db import models

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField('Cart')  # Link to cart items
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    

