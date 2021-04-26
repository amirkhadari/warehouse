from django.contrib import admin
from products.models import Product
# Register your models here.


# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created', 'modified')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProductAdmin)
