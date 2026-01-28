from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    # Основная информация
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(blank=True, verbose_name="Описание")
    address = models.TextField(blank=True, verbose_name="Адрес")
    cover_image = models.ImageField(
        upload_to="project_covers/", blank=True, null=True, verbose_name="Фото обложки"
    )

    # Ссылки и финансы
    google_sheet_url = models.URLField(
        blank=True, verbose_name="Ссылка на Google Таблицу"
    )
    document_url = models.URLField(blank=True, verbose_name="Ссылка на Документы")
    total_cost = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, verbose_name="Общая стоимость (₽)"
    )

    # Участники и документы
    participants = models.ManyToManyField(
        User, related_name="projects", blank=True, verbose_name="Участники проекта"
    )

    # Служебные поля
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_projects",
        verbose_name="Кем обновлено",
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-updated_at"]  # Свежие обновления сверху

    def __str__(self):
        return self.title
