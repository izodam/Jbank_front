from django.urls import path
from . import views

urlpatterns = [
    # API url 이용하여 데이터를 database에 추가
    path('save-deposit-products/', views.save_deposit_products),
    # 정기예금
    path('deposit-products/', views.deposit_products),                              # 전체정보 json 반환
    path('deposit-bank/<str:fin_co_no>/', views.deposit_bank),                      # 은행정보 json 반환
    path('deposit-options/<str:fin_prdt_cd>/', views.deposit_options),              # 상세정보 json 반환
    # 정기적금
    path('saving-products/', views.saving_products),                                # 전체정보 json 반환
    path('saving-bank/<str:fin_co_no>/', views.saving_bank),                        # 은행정보 json 반환
    path('saving-options/<str:fin_prdt_cd>/', views.saving_options),                # 상세정보 json 반환
     # 자유적금
    path('free-saving-products/', views.free_saving_products),                      # 전체정보 json 반환
    path('free-saving-bank/<str:fin_co_no>/', views.free_saving_bank),              # 은행정보 json 반환
    path('free-saving-options/<str:fin_prdt_cd>/', views.free_saving_options),      # 상세정보 json 반환
]
