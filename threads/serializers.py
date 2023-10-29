from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    is_username = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='username.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='username.profile.profile_pic.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_username(self, obj):
        request = self.context['request']
        return request.user == obj.username

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

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
