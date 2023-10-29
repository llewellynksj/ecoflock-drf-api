from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ecoflock_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """

    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('username__post', distinct=True),
        followers_count=Count('username__followed', distinct=True),
        following_count=Count('username__following', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        # profiles following user
        'username__following__followed__profile',
        # profiles followed by user
        'username__followed__username__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'username__following__created_on',
        'username__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """

    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('username__post', distinct=True),
        followers_count=Count('username__followed', distinct=True),
        following_count=Count('username__following', distinct=True)
    ).order_by('-created_on')
