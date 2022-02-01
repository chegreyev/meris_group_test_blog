from rest_framework import serializers

from posts.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'created_by',
            'name',
            'description',
        )


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'created_by',
            'name',
        )


class PostRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'created_by',
            'name',
            'description',
            'likes',
            'dislikes',
        )