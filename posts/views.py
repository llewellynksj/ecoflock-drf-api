from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from ecoflock_api.permissions import IsOwnerOrReadOnly


class PostsList(APIView):
    """
    Gets all posts
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request})
        return Response(serializer.data)
