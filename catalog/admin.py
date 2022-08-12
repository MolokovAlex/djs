from django.contrib import admin

# Register your models here.


from .models import Catalog

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'is_publ')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'name')

admin.site.register(Catalog, CatalogAdmin)

