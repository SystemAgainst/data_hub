from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "total_cost", "updated_at", "updated_by")
    list_filter = ("updated_at", "participants")
    search_fields = ("title", "description")

    # Автоматически подставлять текущего пользователя в поле "Кем обновлено"
    def save_model(self, request, obj, form, change):
        if not change or not obj.updated_by:  # Если создаем или поле пустое
            obj.updated_by = request.user
        obj.save()
