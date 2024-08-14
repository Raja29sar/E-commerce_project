from django.contrib import admin
from .models import Ecommerce

class Ecommerce_Admin(admin.ModelAdmin):
    list_display=['name','number','email']

admin.site.register(Ecommerce,Ecommerce_Admin)

