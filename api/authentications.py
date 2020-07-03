from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from api.models import User


class MyAuth(BaseAuthentication):

    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        if auth is None:
            return None

        auth_list = auth.split()

        if not (len(auth_list) == 2 and auth_list[0].lower() == 'auth'):
            raise AuthenticationFailed('认证信息有误')

        # 解析用户
        if auth_list[1] != 'abc.admin.123':
            raise AuthenticationFailed('用户信息有误')

        user = User.objects.filter(username='admin').first()
        if not user:
            raise AuthenticationFailed('用户不存在')

        return user, None
