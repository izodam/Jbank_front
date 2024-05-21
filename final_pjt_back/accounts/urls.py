# accounts_urls.py
from django.urls import path, include
from .views import join_product, cancel_product, user_profile, update

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('join-product/', join_product, name='join_product'),
    path('cancel-product/', cancel_product, name='cancel_product'),
    path('profile/', user_profile, name='user_profile'),
    path('update/', update, name="update"),
]
