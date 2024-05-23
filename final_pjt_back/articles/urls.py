from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    # 1. GET : 게시글 목록 조회 (json 반환)
    # 2. POST : 신규 게시글 작성완료 버튼 ( form으로 title, content 작성됨 )

    path('articles/<int:article_pk>/', views.article_detail),
    # 1. GET : 게시글 상세 ( 해당 게시글과 댓글들 포함한 json 반환)
    # 2. PUT : 게시글 수정완료 버튼 ( form으로 title, content 작성됨)
    # 3. DELETE : 게시글 삭제 버튼
    # 4. POST : 댓글 작성완료 버튼 ( form으로 content 작성됨 )

    path('articles/<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail),
    # 1. PUT : 댓글 수정완료 버튼 ( form으로 content 작성됨)
    # 2. DELETE : 댓글 삭제 버튼
]