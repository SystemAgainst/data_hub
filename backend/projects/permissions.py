from rest_framework import permissions


class IsProjectParticipantOrAdmin(permissions.BasePermission):
    """
    Правила доступа:
    1. Админ: Полный доступ (чтение, изменение, удаление).
    2. Гость (не авторизован): Видит только список (list), но не детали (retrieve).
    3. Авторизованный пользователь:
       - Если "Постоянный" (is_staff): Видит всё.
       - Если "Участник": Видит только свои проекты.
    """

    def has_permission(self, request, view):
        # Глобальное право на доступ к эндпоинту

        # 1. Админы и Персонал (Постоянные) могут всё
        if request.user.is_superuser or request.user.is_staff:
            return True

        # 2. Список проектов (витрина) доступна всем, даже Гостям
        if view.action == "list":
            return True

        # 3. Детали (провалиться в карточку) доступны только авторизованным
        if view.action == "retrieve":
            return request.user.is_authenticated

        # 4. Создавать/Удалять/Менять - только админы (пока так)
        return False

    def has_object_permission(self, request, view, obj):
        # Право на доступ к конкретному объекту (когда уже провалились)

        # 1. Админы и Персонал видят любой проект
        if request.user.is_superuser or request.user.is_staff:
            return True

        # 2. Обычный участник видит проект, ТОЛЬКО если он в списке participants
        if request.user.is_authenticated:
            return request.user in obj.participants.all()

        # 3. Гости сюда не дойдут (отсеются на has_permission), но на всякий случай
        return False
