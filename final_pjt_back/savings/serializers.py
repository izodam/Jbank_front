# savings_serializers.py
from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions


# openAPI 서버에서 db로 저장하기 위해 만들어진 serializer

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'



# db에 있는 예금 데이터를 입맛대로 json 형태로 만들기 위한 serializer, ChatGPT 사용

class DepositOptionsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = ['save_trm', 'intr_rate', 'intr_rate2']  # 필드 목록: 저축 기간, 저축 금리, 최고 우대금리

class DepositProductsSerializer2(serializers.ModelSerializer):
    options = DepositOptionsSerializer2(source='depositoptions_set', many=True, read_only=True)  # DepositOptions와의 관계 설정

    def to_representation(self, instance):
        representation = super().to_representation(instance)  # 기본 표현을 가져옴
        options = representation.pop('options')  # 옵션 데이터를 가져옴

        # 각 기간에 대한 금리 저장용 딕셔너리 초기화
        terms = {
            1: {'before': 0.0, 'after': 0.0},
            3: {'before': 0.0, 'after': 0.0},
            6: {'before': 0.0, 'after': 0.0},
            12: {'before': 0.0, 'after': 0.0},
            24: {'before': 0.0, 'after': 0.0},
            36: {'before': 0.0, 'after': 0.0},
        }

        max_before = 0.0  # 최대 금리 (저축 금리)
        max_after = 0.0  # 최대 금리 (최고 우대금리)

        # 각 옵션에 대해 금리 계산
        for option in options:
            save_trm = option['save_trm']
            if save_trm in terms:
                terms[save_trm]['before'] = max(terms[save_trm]['before'], option['intr_rate'])  # 기간별 최대 저축 금리 갱신
                terms[save_trm]['after'] = max(terms[save_trm]['after'], option['intr_rate2'])  # 기간별 최대 최고 우대금리 갱신
                max_before = max(max_before, option['intr_rate'])  # 전체 최대 저축 금리 갱신
                max_after = max(max_after, option['intr_rate2'])  # 전체 최대 최고 우대금리 갱신

        # 각 기간에 대한 금리를 표현에 추가
        for term, rates in terms.items():
            representation[f"{term}month_before"] = rates['before']
            representation[f"{term}month_after"] = rates['after']

        representation['max_before'] = max_before  # 전체 최대 저축 금리 추가
        representation['max_after'] = max_after  # 전체 최대 최고 우대금리 추가

        return representation

    class Meta:
        model = DepositProducts
        fields = '__all__'  # 모든 필드를 포함



# db에 있는 적금 데이터를 입맛대로 json 형태로 만들기 위한 serializer, ChatGPT 사용

class SavingOptionsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = ['save_trm', 'intr_rate', 'intr_rate2']

class SavingProductsSerializer2(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    def get_options(self, obj):
        rsrv_type = self.context.get('rsrv_type')
        options = obj.savingoptions_set.filter(rsrv_type=rsrv_type)
        return SavingOptionsSerializer2(options, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        options = representation.pop('options')

        terms = {
            1: {'before': 0.0, 'after': 0.0},
            3: {'before': 0.0, 'after': 0.0},
            6: {'before': 0.0, 'after': 0.0},
            12: {'before': 0.0, 'after': 0.0},
            24: {'before': 0.0, 'after': 0.0},
            36: {'before': 0.0, 'after': 0.0},
        }

        max_before = 0.0
        max_after = 0.0

        for option in options:
            save_trm = option['save_trm']
            if save_trm in terms:
                terms[save_trm]['before'] = max(terms[save_trm]['before'], option['intr_rate'])
                terms[save_trm]['after'] = max(terms[save_trm]['after'], option['intr_rate2'])
                max_before = max(max_before, option['intr_rate'])
                max_after = max(max_after, option['intr_rate2'])

        for term, rates in terms.items():
            representation[f"{term}month_before"] = rates['before']
            representation[f"{term}month_after"] = rates['after']

        representation['max_before'] = max_before
        representation['max_after'] = max_after

        return representation

    class Meta:
        model = SavingProducts
        fields = '__all__'


from accounts.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'