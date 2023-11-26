from rest_framework import serializers

from .models import ForumPost, Reply


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'body', 'creation_date', 'update_date', 'author', 'like_count']
        read_only_fields = ['author', 'like_count']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'post', 'author', 'body', 'creation_date', 'update_date']
