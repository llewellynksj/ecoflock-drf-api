from rest_framework import serializers
from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')

    class Meta:
        model = Favourite
        fields = [
            'id',
            'username',
            'post',
            'created_on',
        ]
