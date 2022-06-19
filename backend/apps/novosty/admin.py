from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id']
    prepopulated_fields = {"slug":('name',)}

    search_fields = (
        "id",
        "name",
    )

@admin.register(Novosty)
class NovostyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image',
        'category',
        'created',
        'updated',
    ]
