from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostCreateSerializer, PostListSerializer, PostRetrieveSerializer, GradeCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def get_serializer_class(self):
        serializer = self.serializer_class

        if self.action == 'list':
            serializer = PostListSerializer
        elif self.action == 'retrieve':
            serializer = PostRetrieveSerializer
        elif self.action == 'like':
            serializer = GradeCreateSerializer

        return serializer

    @action(methods=['POST'], detail=True, url_path='like')
    def like(self, request, *args, **kwargs):
        instance = self.get_object()
        # TODO: проверять были ли оценки от этого пользователя и при надобности менять их
        instance.grades.create(is_liked=True, created_by=self.request.user)
        return Response(status=200)
