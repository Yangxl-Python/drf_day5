from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle

from api.authentications import MyAuth
from api.models import User
from api.permissions import MyPermission
from api.throttlings import SendMessageRate
from utils.response import APIResponse


class TestAPIView(APIView):

    authentication_classes = [MyAuth]

    def get(self, request, *args, **kwargs):
        user = User.objects.first()
        # 查询用户
        print(user)

        # 根据用户获取对应的角色
        print(user.groups.first())

        # 据用户获取对应的权限
        print(user.user_permissions.first().name)

        # 获取角色
        group = Group.objects.first()
        print(group)

        # 根据角色获取对应的权限
        print(group.permissions.first().name)

        # 根据角色获取对应的用户
        print(group.user_set.first())

        # 获取权限
        permission = Permission.objects.first()
        print(permission.name)

        # 根据权限获取对应的用户
        print(permission.user_set.first())

        # 根据权限获取对应的角色
        print(permission.group_set.first().name)

        return APIResponse('ok')


class TestPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse('success')


class UserLoginOrReadonly(APIView):
    # authentication_classes = [MyAuth]
    # permission_classes = [MyPermission]
    throttle_classes = [UserRateThrottle]
    # scope = 'login'

    def get(self, request, *args, **kwargs):
        return APIResponse('读操作')

    def post(self, request, *args, **kwargs):
        return APIResponse('写操作')


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse('ok')
