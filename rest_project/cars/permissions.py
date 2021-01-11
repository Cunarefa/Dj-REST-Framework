from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

# Когда сюда приходит запрос, он проверяет - это метод безопасный или нет. Безопасные
# методы это GET, HEAD, OPTIONS и вернет True - значит можно что то делать. Если не
# безопасн метод, то он сравнит - равен ли польз-ль польз-телю этой записи
