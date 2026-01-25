from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Project
from .permissions import IsProjectParticipantOrAdmin
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет смотреть и редактировать проекты.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # Опционально: Можно переопределить get_serializer_class,
    # чтобы Гостям отдавать "урезанный" JSON (без цены и ссылок),
    # а Своим - полный. Это best practice для безопасности.
    permission_classes = [IsProjectParticipantOrAdmin]
