from django.contrib import admin
from product.models import Item
class Item_Admin(admin.ModelAdmin):
    list_display=['Pid','Pname','Pprice','Pimg','Pmfg']
admin.site.register(Item,Item_Admin)    

