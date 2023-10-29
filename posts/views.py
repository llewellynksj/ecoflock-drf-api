from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Post.objects.annotate(
        threads_count=Count('username__thread', distinct=True),
        favourites_count=Count('username__favourite', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # users feed of followed users posts
        'username__followed__username__profile',
        # user liked posts
        'favourites__username__profile',
        # users posts
        'username__profile',
    ]
    search_fields = [
        'username__username',
        'title',
        'topic_category',
        'other_tags',
    ]
    ordering_fields = [
        'threads_count',
        'favourites_count',
        'favourites__created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Individual profile view
    Retrieves post details, allows logged in user to update and delete posts
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        threads_count=Count('username__thread', distinct=True),
        favourites_count=Count('username__favourite', distinct=True),
    ).order_by('-created_on')
