from django.contrib import admin

# Register your models here.


from .models import Catalog, Seller

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'seller', 'create_at', 'update_at', 'is_publ')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'name')
    list_editable = ('is_publ',)
    list_filter = ('seller', 'is_publ')

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller_name')
    list_display_links = ('id', 'seller_name')
    search_fields = ('seller_name',)

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Seller, SellerAdmin)

