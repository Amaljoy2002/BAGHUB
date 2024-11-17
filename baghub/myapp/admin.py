from django.contrib import admin
from .models import CustomUser 
from .models import Product ,Category
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Category)