from rest_framework import generics, permissions
from ecoflock_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    Post list view
    Retrieves all posts and allows posts to be made by logged in user
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Individual profile view
    Retrieves post details, allows logged in user to update and delete posts
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
