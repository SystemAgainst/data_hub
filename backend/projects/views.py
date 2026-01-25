from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет смотреть и редактировать проекты.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # Разрешаем читать всем (даже анонимам пока), а менять - только авторизованным
    permission_classes = [IsAuthenticatedOrReadOnly]
