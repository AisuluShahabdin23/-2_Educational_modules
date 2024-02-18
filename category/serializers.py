from rest_framework import serializers
from category.models import Category
from module.models import Module
from module.serializers import ModuleSerializer


class CategorySerializer(serializers.ModelSerializer):
    """ Класс сериализатор категорий """
    count_modules = serializers.SerializerMethodField()
    modules = ModuleSerializer(source='modules_set', read_only=True, many=True)

    def get_count_modules(self, obj):
        return Module.objects.filter(id_category=obj).count()

    class Meta:
        model = Category
        fields = ("id", "title", "description", "photo", "count_modules", 'modules')
