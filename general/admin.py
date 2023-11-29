from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "price",
    )
    fields = (
        "name",
        "description",
        "price",
    )
    search_fields = (
        "name",
        "author__name",
    )
