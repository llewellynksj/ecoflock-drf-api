from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    is_user = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.username

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                username=user, followed=obj.username).first()
            return following.id if following else None
        return None

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
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
        ]
