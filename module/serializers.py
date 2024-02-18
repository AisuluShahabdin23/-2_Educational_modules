from rest_framework import serializers
from module.models import Module


class ModuleSerializer(serializers.ModelSerializer):
    """ Класс сериализатор образовательного модуля """
    count_users = serializers.SerializerMethodField()
    list_uu = serializers.SerializerMethodField()

    def get_count_users(self, obj):
        return obj.id_users.count()

    def get_list_uu(self, obj):
        return str([f"{u.email, u.phone}" for u in obj.id_users.all()])

    class Meta:
        model = Module
        fields = ("id", "title", "description", "photo", "id_category", "id_users", "count_view", "count_users",
                  "list_uu", )
