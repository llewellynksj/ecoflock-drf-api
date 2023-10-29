from rest_framework import serializers
from .models import Post
from favourites.models import Favourite


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    is_username = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='username.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='username.profile.profile_pic.url')
    favourite_id = serializers.SerializerMethodField()
    threads_count = serializers.ReadOnlyField()
    favourites_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Error! Please upload an image below 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Error! Please upload an image with width below 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Error! Please upload an image with height below 4096px'
            )
        return value

    def get_is_username(self, obj):
        request = self.context['request']
        return request.user == obj.username

    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                username=user, post=obj).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'username',
            'created_on',
            'updated_on',
            'title',
            'topic_category',
            'other_tags',
            'image',
            'url',
            'content',
            'is_username',
            'profile_id',
            'profile_image',
            'favourite_id',
            'threads_count',
            'favourites_count',
        ]
