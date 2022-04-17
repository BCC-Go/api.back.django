from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from .serializers import UserSeriallizers
from .models import User


class UserViewSet(GenericViewSet):
    
    @action(detail=False, methods=['get'])
    def test(self, request):
        return 1
    queryset = User.objects.all()
    print(queryset)
    print()
    print()
    print(UserSeriallizers(queryset[0]))
