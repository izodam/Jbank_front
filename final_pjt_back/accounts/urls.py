# accounts_urls.py
from django.urls import path, include
from .views import join_product, cancel_product, user_profile, update, hot_products

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('join-product/', join_product, name='join_product'),           # 상품 가입 버튼 클릭
    path('cancel-product/', cancel_product, name='cancel_product'),     # 가입 취소 버튼 클릭
    path('profile/', user_profile, name='user_profile'),                # 프로필 접근시 주어질 json
    path('update/', update, name="update"),                             # 회원 정보 수정 클릭
    path('hot-products/', hot_products),                          # 많이 가입한 상품 10개와 그 차트
]
