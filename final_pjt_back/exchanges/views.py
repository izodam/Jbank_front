import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ExchangeRates
from .serializers import ExchangeRatesSerializer


@api_view(['GET'])
def index(request):
    exchange_api_key = settings.EXCHANGE_API_KEY
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={exchange_api_key}&data=AP01'
    response = requests.get(url).json()             # api에 서버에 있는거 가져와서 정렬
    sorted_response = sorted(response, key=lambda x: x['cur_nm'])
    exchange_db = ExchangeRates.objects.all()       # db에 있는거 불러오기

    if sorted_response:                             # 서버 데이터가 있고
        if exchange_db:                             # db에도 데이터가 있다면
            ExchangeRates.objects.all().delete()    # db 삭제
        
        serializer = ExchangeRatesSerializer(data=sorted_response, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    # 서버에 데이터가 없다면 db에서 가져오기
    serializer = ExchangeRatesSerializer(exchange_db, many=True)
    return Response(serializer.data)
