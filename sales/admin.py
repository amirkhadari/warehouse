from django.contrib import admin
from sales.models import CSV, Sale, Position
# Register your models here.


# admin.site.register(Position)
# admin.site.register(CSV)
# admin.site.register(Sale)


class CSVAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'created', 'updated')
    search_fields = ('file_name', )


class SaleAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'get_positions', 'total_price',
                    'customer', 'sales_man')
    search_fields = ('transaction_id', 'customer', 'sales_man', )


class PositionAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'quantity', 'price', )
    search_fields = ('get_product_name', )


admin.site.register(Position, PositionAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(CSV, CSVAdmin)
