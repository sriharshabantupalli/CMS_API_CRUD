from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from .permissions import IsOwnerOrReadOnly

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer