# accounts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import UserSerializer, ProductSerializer, generate_combined_chart
from savings.models import DepositProducts, SavingProducts

User = get_user_model()

@api_view(['POST'])
def join_product(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    prdt_type = request.data.get('prdt_type')
    fin_prdt_cd = request.data.get('fin_prdt_cd')

    if not all([prdt_type, fin_prdt_cd]):
        return Response({'detail': 'Missing required parameters.'}, status=status.HTTP_400_BAD_REQUEST)

    if prdt_type == 'deposit':
        product_data = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    elif prdt_type == 'saving':
        product_data = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    else:
        return Response({'detail': 'Invalid product type.'}, status=status.HTTP_400_BAD_REQUEST)

    Product.objects.create(
        user=user,
        prdt_type=prdt_type,
        fin_prdt_cd=fin_prdt_cd,
        fin_prdt_nm=product_data.fin_prdt_nm,
        kor_co_nm=product_data.kor_co_nm
    )
    return Response({'detail': f'Joined {prdt_type} product successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def cancel_product(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)

    prdt_type = request.data.get('prdt_type')
    fin_prdt_cd = request.data.get('fin_prdt_cd')
    if not all([prdt_type, fin_prdt_cd]):
        return Response({'detail': 'Missing required parameters.'}, status=status.HTTP_400_BAD_REQUEST)

    product = get_object_or_404(Product, user=user, prdt_type=prdt_type, fin_prdt_cd=fin_prdt_cd)
    product.delete()
    return Response({'detail': f'Cancelled {prdt_type} product successfully.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_profile(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'detail': 'Authentication required or access denied.'}, status=status.HTTP_401_UNAUTHORIZED)

    products = Product.objects.filter(user=user)
    product_serializer = ProductSerializer(products, many=True)
    user_serializer = UserSerializer(user)

    chart_base64 = generate_combined_chart(product_serializer.data)

    return Response({
        'user': user_serializer.data,
        'products': product_serializer.data,
        'chart': chart_base64
    })


@api_view(['PUT'])
def update(request):
    user = request.user
    if not user.is_authenticated:
        return Response({'detail': 'Authentication required or access denied.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

