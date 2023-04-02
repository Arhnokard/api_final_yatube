from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import pagination
from rest_framework import permissions
from rest_framework import viewsets

from posts.models import Post, Group
from .permissions import AuthorEditOrReadOnly
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorEditOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorEditOrReadOnly,)

    def get_queryset(self):
        post =get_object_or_404(Post, id=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()
        return new_queryset
    
    def perform_create(self, serializer):
        post =get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
