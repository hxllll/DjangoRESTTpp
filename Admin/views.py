from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView

from Admin.models import AdminUser
from Admin.serializers import AdminUserSerializer


class AdminUsersAPIView(CreateAPIView):

    serializer_class = AdminUserSerializer

    def post(self, request, *args, **kwargs):

        action = request.query_params.get("action")

        if action == 'register':
            return self.create(request,*args,**kwargs)
        elif action == 'login':
            a_username = request.data.get("a_username")
            a_password = request.data.get("a_password")

            users = AdminUser.objects.filter(a_username = a_username)

            if not users.exists():
                raise APIException(detail="用户不存在")

            user = users.first()