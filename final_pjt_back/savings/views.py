import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer
from .serializers import DepositProductsSerializer2, SavingProductsSerializer2, ProductSerializer
from .models import DepositProducts, SavingProducts
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import Product
from django.db.models import Count

User = get_user_model()

# OpenAPI -> DB
@api_view(['GET'])
def save_deposit_products(request):
    saving_api_key = settings.SAVING_API_KEY

    # 1. 예금 API url 통해서 json 추출
    deposit_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={saving_api_key}&topFinGrpNo=020000&pageNo=1'
    deposit_response = requests.get(deposit_url).json()

    # 1-1. 예금 베이스 데이터 저장
    for li in deposit_response.get('result').get('baseList'):
        serializer = DepositProductsSerializer(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 1-2. 예금 옵션 데이터 저장
    for li in deposit_response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd).pk
        save_data = {'product': product}
        save_data.update(li)
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 2. 적금 API url 통해서 json 추출
    saving_url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={saving_api_key}&topFinGrpNo=020000&pageNo=1'
    saving_response = requests.get(saving_url).json()

    # 2-1. 적금 베이스 데이터 저장
    for li in saving_response.get('result').get('baseList'):
        serializer = SavingProductsSerializer(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 2-2. 적금 옵션 데이터 저장
    for li in saving_response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd).pk
        save_data = {'product': product}
        save_data.update(li)
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return Response({"message": "데이터 저장/업데이트 완료"}, status=status.HTTP_200_OK)



# 예금
@api_view(['GET'])
def deposit_products(request):
    products = DepositProducts.objects.all()
    serializers = DepositProductsSerializer2(products, many=True)
    sorted_data = sorted(serializers.data, key=lambda x: x['max_after'], reverse=True)
    return Response(sorted_data)

# 예금 은행별로 추출
@api_view(['GET'])
def deposit_bank(request, fin_co_no):
    products = DepositProducts.objects.filter(fin_co_no=fin_co_no)
    serializers = DepositProductsSerializer2(products, many=True)
    sorted_data = sorted(serializers.data, key=lambda x: x['max_after'], reverse=True)
    return Response(sorted_data)

# 예금 detail
@api_view(['GET'])
def deposit_options(request, fin_prdt_cd):
    user = request.user
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer2(product)

    is_joined = False
    if user.is_authenticated:
        is_joined = Product.objects.filter(user=user, prdt_type='deposit', fin_prdt_cd=fin_prdt_cd).exists()

    return Response({
        'data': serializer.data,
        'isjoined': is_joined
    })



# 정기적금
@api_view(['GET'])
def saving_products(request):
    products = SavingProducts.objects.filter(savingoptions__rsrv_type='S').distinct()
    serializers = SavingProductsSerializer2(products, many=True, context={'rsrv_type': 'S'})
    sorted_data = sorted(serializers.data, key=lambda x: x['max_after'], reverse=True)
    return Response(sorted_data)

# 정기적금 은행별로 추출
@api_view(['GET'])
def saving_bank(request, fin_co_no):
    products = SavingProducts.objects.filter(fin_co_no=fin_co_no, savingoptions__rsrv_type='S').distinct()
    serializers = SavingProductsSerializer2(products, many=True, context={'rsrv_type': 'S'})
    sorted_data = sorted(serializers.data, key=lambda x: x['max_after'], reverse=True)
    return Response(sorted_data)

# 정기적금 detail
@api_view(['GET'])
def saving_options(request, fin_prdt_cd):
    user = request.user
    product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer2(product, context={'rsrv_type': 'S'})

    is_joined = False
    if user.is_authenticated:
        is_joined = Product.objects.filter(user=user, prdt_type='saving', fin_prdt_cd=fin_prdt_cd).exists()

    return Response({
        'data': serializer.data,
        'isjoined': is_joined
    })



# 자유적금
@api_view(['GET'])
def free_saving_products(request):
    products = SavingProducts.objects.filter(savingoptions__rsrv_type='F').distinct()
    serializers = SavingProductsSerializer2(products, many=True, context={'rsrv_type': 'F'})
    sorted_data = sorted(serializers.data, key=lambda x: x['max_after'], reverse=True)
    return Response(sorted_data)

# 자유적금 은행별로 추출
@api_view(['GET'])
def free_saving_bank(request, fin_co_no):
    products = SavingProducts.objects.filter(fin_co_no=fin_co_no, savingoptions__rsrv_type='F').distinct()
    serializer = SavingProductsSerializer2(products, many=True, context={'rsrv_type': 'F'})
    sorted_data = sorted(serializer.data, key=lambda x: x['max_after'], reverse=True)
    return Response(sorted_data)

# 자유적금 detail
@api_view(['GET'])
def free_saving_options(request, fin_prdt_cd):
    user = request.user
    product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer2(product, context={'rsrv_type': 'F'})

    is_joined = False
    if user.is_authenticated:
        is_joined = Product.objects.filter(user=user, prdt_type='saving', fin_prdt_cd=fin_prdt_cd).exists()

    return Response({
        'data': serializer.data,
        'isjoined': is_joined
    })



@api_view(['GET'])
def recommend_products(request):
    if not request.user.is_authenticated:
        return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
    
    user = request.user
    age_range = (user.age - 10, user.age + 10)
    salary_range = (user.salary - 10000000, user.salary + 10000000)
    money_range = (user.money - 10000000, user.money + 10000000)
    
    similar_users = User.objects.filter(
        age__range=age_range,
        salary__range=salary_range,
        money__range=money_range
    )
    
    recommended_products = Product.objects.filter(
        user__in=similar_users
    ).annotate(
        num_users=Count('user')
    ).order_by('-num_users')[:3]
    
    serializer = ProductSerializer(recommended_products, many=True)
    return Response({
        'data': serializer.data,
    })