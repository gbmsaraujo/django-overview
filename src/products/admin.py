from django.contrib import admin
from .models import Product

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("title", "price")  # Campos exibidos na lista
    list_filter = ("title", "price")  # Filtros disponíveis na barra lateral
    search_fields = ("title",)  # Campo de pesquisa

admin.site.register(Product, ProdutoAdmin)
