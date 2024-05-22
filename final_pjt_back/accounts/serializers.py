# accounts_serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product
from savings.models import DepositProducts, SavingProducts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

import matplotlib
matplotlib.use('Agg')

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'nickname', 'age', 'salary', 'money']


class ProductSerializer(serializers.ModelSerializer):
    max_before = serializers.SerializerMethodField()
    max_after = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['user', 'prdt_type', 'fin_prdt_cd', 'fin_prdt_nm', 'kor_co_nm', 'max_before', 'max_after']

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

def generate_combined_chart(products):
    labels = []
    max_befores = []
    max_afters = []

    for product in products:
        labels.append(product['fin_prdt_nm'])
        max_befores.append(product['max_before'])
        max_afters.append(product['max_after'])

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width/2, max_befores, width, label='저축 금리', color='#578dbe')
    rects2 = ax.bar(x + width/2, max_afters, width, label='최고 우대금리', color='#1B3074')

    ax.set_xlabel('상품명')
    ax.set_ylabel('금리')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    image_base64 = base64.b64encode(image_png).decode('utf-8')
    return image_base64
