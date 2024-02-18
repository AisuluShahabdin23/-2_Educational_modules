from django.contrib import admin
from module.models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("id_category",)
    search_fields = ("title",)
