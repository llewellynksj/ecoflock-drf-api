from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.username

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'created_on',
            'first_name',
            'last_name',
            'profile_pic',
            'is_user',
        ]
