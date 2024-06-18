from django.contrib import admin
from .models import Product, Category, Blog


admin.site.register([Product, Category, Blog])



