from rest_framework import serializers
from .models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    is_username = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='username.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='username.profile.profile_pic.url')

    def get_is_username(self, obj):
        request = self.context['request']
        return request.user == obj.username

    class Meta:
        model = Thread
        fields = [
            'id',
            'username',
            'is_username',
            'profile_id',
            'profile_image',
            'post',
            'created_on',
            'updated_on',
            'comment',
        ]


class ThreadDetailSerializer(ThreadSerializer):
    post = serializers.ReadOnlyField(source='post.id')
