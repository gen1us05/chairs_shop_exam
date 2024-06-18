from django.contrib import admin
from .models import Customer, Comments, Workers


admin.site.register([Customer, Comments, Workers])


