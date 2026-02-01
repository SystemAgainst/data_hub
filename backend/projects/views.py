from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# Добавьте эти импорты для логина:
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Project
from .permissions import IsProjectParticipantOrAdmin
from .serializers import ProjectSerializer
from .services import get_sheet_stats


class CustomAuthToken(ObtainAuthToken):
    """
    Кастомная вьюха для логина.
    Отключает authentication_classes, чтобы игнорировать
    Cookie сессии (если админ залогинен в браузере) и не требовать CSRF.
    """

    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                # Можно вернуть еще ID или имя, если нужно на фронте
                "user_id": user.pk,
                "username": user.username,
            }
        )


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет смотреть и редактировать проекты.
    """

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer
    permission_classes = [IsProjectParticipantOrAdmin]

    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        print(
            f"DEBUG: User: {user.username}, Is Super: {user.is_superuser}, Is Staff: {user.is_staff}"
        )
        if not user.is_authenticated:
            return Project.objects.none()

        # Оставляем доступ ко всем проектам ТОЛЬКО Суперпользователю (admin)
        if user.is_superuser:
            return Project.objects.all()

        # Для всех остальных — только их проекты
        return Project.objects.filter(participants=user)

    @action(detail=True, methods=["get"])
    def stats(self, request, pk=None):
        # ... (ваш код stats остается без изменений)
        project = self.get_object()
        # get_object сам вызовет get_queryset, так что проверка прав сработает и тут

        if not project.google_sheet_url:
            return Response({"error": "No Google Sheet linked"}, status=400)

        data = get_sheet_stats(project.google_sheet_url)
        if not data:
            return Response({"error": "Failed to fetch data"}, status=502)

        return Response(data)
