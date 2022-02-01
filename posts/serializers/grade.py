from rest_framework import serializers

from posts.models import Grade


class GradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'created_by',
            'is_like',
            'post',
        )
