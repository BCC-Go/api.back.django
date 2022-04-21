from django.shortcuts import render
from rest_framework.viewsets import (
    GenericViewSet,
    mixins,
)
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSeriallizers
from .models import User


class UserViewSet(GenericViewSet):
    """
    # User 관련 API set
    ---
    - accounts/login (post) : 로그인 API
    - accounts/logout (post) : 로그아웃 API
    """

    queryset = User.objects.all()
    serializer_class = UserSeriallizers
    http_method_names = ["get", "post", "delete", "patch"]

    @action(detail=False, methods=["get"])
    def login(self, request):
        """
        # login api
        ---
        - ## body
            - ### test
        - ## response
        """
        print("test!!!!!!")
        return Response({"message": "success"})

    
    @action(detail=False, methods=["post"])
    def logout(self,request):
        """
        # test
        ---

        """
        tmp = User.objects.get(login_id = request.data.get("login_id"))
        print(tmp)
        print(UserSeriallizers(User.objects.all()[1]).data)
        print(UserSeriallizers(tmp).data['id'])
        print(request.data.get("login_id"))
        
        return Response({"message": "success"})
