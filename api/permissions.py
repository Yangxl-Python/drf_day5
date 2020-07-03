from rest_framework.permissions import BasePermission

from api.models import User


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        username = request.data.get('username')
        user = User.objects.filter(username=username)
        if user:
            return True
        return False
