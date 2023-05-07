from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    '''
    Разрешение, что только суперюзер и администратор
    могут просматривать, изменять и удалять контент.
    '''

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    '''
    Только суперюзер и администратор могут изменять и удалять контент,
    для остальных пользователей доступно только чтение.
    '''

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin)


class IsAdminOrAuthorOrReadOnly(permissions.BasePermission):
    '''
    Только суперюзер, администратор, модератор и автор могут изменять
    и удалять контент, для остальных пользователей доступно только чтение.
    Post запрос может делать только пользователь, прошедший аутентификацию.
    '''

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_admin
                     or request.user.is_moderator
                     or request.user == obj.author))
