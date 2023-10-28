from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='author.profile.profile_pic.url')

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

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'created_on',
            'updated_on',
            'title',
            'topic_category',
            'other_tags',
            'image',
            'url',
            'content',
            'is_author',
            'profile_id',
            'profile_image',
        ]
