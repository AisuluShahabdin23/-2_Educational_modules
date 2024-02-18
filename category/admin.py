from django.contrib import admin
from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("title",)
    search_fields = ("title",)
