from rest_framework import serializers

from .models import User

class UserSeriallizers(serializers.ModelSerializer):
    class Meta:
        model = User
        field = (
            'id',
            'rank_id',
            'login_id',
            'password',
            'phone',
            'sex',
            'birth',
            'consumption',
            'address',
            'type',
        )
