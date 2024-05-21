# accounts_serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product
from savings.models import DepositProducts, SavingProducts

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'salary', 'money']

class ProductSerializer(serializers.ModelSerializer):
    max_before = serializers.SerializerMethodField()
    max_after = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['user', 'prdt_type', 'fin_prdt_cd', 'fin_prdt_nm', 'max_before', 'max_after']

    def get_max_before(self, obj):
        if obj.prdt_type == 'deposit':
            product = DepositProducts.objects.get(fin_prdt_cd=obj.fin_prdt_cd)
            return max([opt.intr_rate for opt in product.depositoptions_set.all()], default=0.0)
        elif obj.prdt_type == 'saving':
            product = SavingProducts.objects.get(fin_prdt_cd=obj.fin_prdt_cd)
            return max([opt.intr_rate for opt in product.savingoptions_set.all()], default=0.0)
        return 0.0

    def get_max_after(self, obj):
        if obj.prdt_type == 'deposit':
            product = DepositProducts.objects.get(fin_prdt_cd=obj.fin_prdt_cd)
            return max([opt.intr_rate2 for opt in product.depositoptions_set.all()], default=0.0)
        elif obj.prdt_type == 'saving':
            product = SavingProducts.objects.get(fin_prdt_cd=obj.fin_prdt_cd)
            return max([opt.intr_rate2 for opt in product.savingoptions_set.all()], default=0.0)
        return 0.0
