from rest_framework import generics, permissions
from ecoflock_api.permissions import IsOwnerOrReadOnly
from .models import Thread
from .serializers import ThreadSerializer, ThreadDetailSerializer


class ThreadList(generics.ListCreateAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Thread.objects.all()

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ThreadDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Thread.objects.all()
