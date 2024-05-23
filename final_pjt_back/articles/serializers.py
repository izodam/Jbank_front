from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

    def get_username(self, obj):
        return obj.user.username

    def get_nickname(self, obj):
        return obj.user.nickname


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)

    def get_username(self, obj):
        return obj.user.username

    def get_nickname(self, obj):
        return obj.user.nickname
