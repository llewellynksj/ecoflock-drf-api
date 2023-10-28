from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from ecoflock_api.permissions import IsOwnerOrReadOnly


class PostList(APIView):
    """
    Post list view
    Retrieves all posts and allows posts to be made by logged in user
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        """
        Retrieves all posts
        """
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """
        Allows a post to be made
        """
        serializer = PostSerializer(
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Individual profile view
    Retrieves post details, allows logged in user to update and delete posts
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Checks requested post exists
        """
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Returns serialized data for requested post
        """
        post = self.get_object(pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Allows updates to be made to post if user is valid
        """
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes post
        """
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
