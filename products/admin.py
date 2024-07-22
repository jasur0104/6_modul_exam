from django.contrib import admin
from .models import Category,Products
from import_export.admin import ImportExportModelAdmin
@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
     list_display = ('name','price','category','description')
     list_display_links = ('name','price')
     search_fields = ('name',)
     ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
     list_display = ('name',)
     list_display_links = ('name',)
     search_fields = ('name',)
     ordering = ('name',)

