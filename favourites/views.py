from rest_framework import generics, permissions
from ecoflock_api.permissions import IsOwnerOrReadOnly
from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Favourite.objects.all()
