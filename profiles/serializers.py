from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'username', 'created_on', 'first_name', 'last_name', 'profile_pic',
        ]
