from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_staff"]


class ProjectSerializer(serializers.ModelSerializer):
    # Добавляем поле, чтобы видеть имя того, кто обновил, текстом, а не ID
    updated_by_name = serializers.ReadOnlyField(source="updated_by.username")
    participants_details = UserMiniSerializer(
        source="participants", many=True, read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "address",
            "documents",
            "cover_image",
            "google_sheet_url",
            "total_cost",
            "updated_at",
            "updated_by_name",
            "updated_by",
            "participants",
            "participants_details",
        ]

        read_only_fields = ["updated_by", "created_at", "updated_at"]

    # Автоматическое сохранение того, кто редактировал
    def update(self, instance, validated_data):
        # При обновлении записываем текущего юзера
        user = self.context["request"].user
        if user.is_authenticated:
            instance.updated_by = user
        return super().update(instance, validated_data)
