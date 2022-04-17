from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSeriallizers
from .models import User


def UserViewSet(GenericViewSet):
    
    queryset = User.objects.all()
    print(queryset)
    print(UserSeriallizers(queryset))
