from rest_framework import generics, permissions
from drf.permissions import isOwnerOrReadOnly
from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer

class Comment(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)
