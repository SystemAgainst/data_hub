from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # Добавляем поле, чтобы видеть имя того, кто обновил, текстом, а не ID
    updated_by_name = serializers.CharField(
        source="updated_by.username", read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "cover_image",
            "google_sheet_url",
            "total_cost",
            "updated_at",
            "updated_by_name",
        ]
