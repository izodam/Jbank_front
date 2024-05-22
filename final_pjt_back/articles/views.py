from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        comments = Comment.objects.filter(article=article)
        comments_serializer = CommentSerializer(comments, many=True)
        return Response({
            'article': serializer.data,
            'comments': comments_serializer.data
        })
    
    elif request.method == 'PUT':
        if article.user != request.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if article.user != request.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        data = request.data.copy()
        data['article'] = article_pk
        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, article_id=article_pk, pk=comment_pk)

    if request.method == 'PUT':
        if comment.user != request.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if comment.user != request.user:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)