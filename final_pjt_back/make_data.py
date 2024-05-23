import random
import json
from collections import OrderedDict
from datetime import datetime, timezone, timedelta
from django.utils.crypto import get_random_string

# 랜덤한 이름 생성
def random_name():
    result = ''
    result += random.choice('김이박최정강조윤장임')
    result += random.choice('민서예지도하주윤채현지')
    result += random.choice('준윤우원호후서연아은진')
    return result

# 랜덤 이메일 생성
def random_email():
    domains = ["example.com", "test.com", "sample.com"]
    return get_random_string(10) + "@" + random.choice(domains)

# JSON 파일 만들기
user_file = OrderedDict()
product_file = OrderedDict()

N = 1000  # 생성할 유저 수
M = 5   # 가입할 상품 수
users = []
products = []

# 시간대 설정
tz = timezone(timedelta(hours=0))  # UTC 시간대

# 유저 데이터 생성
for i in range(N):
    name = random_name()
    user = OrderedDict()
    user['model'] = 'accounts.user'
    user['pk'] = i + 1
    user['fields'] = {
        'username': f"user{i+5}",
        'password': 'pbkdf2_sha256$260000$' + get_random_string(12) + '$' + get_random_string(32),  # 랜덤한 해시 비밀번호
        'last_login': datetime.now(tz).isoformat(),
        'is_superuser': False,
        'first_name': name[0],
        'last_name': name[1:],
        'email': random_email(),
        'is_staff': False,
        'is_active': True,
        'date_joined': datetime.now(tz).isoformat(),
        'nickname': random.choice([None, name+str(random.randint(1, 100))]),
        'age': random.randint(18, 80),
        'money': random.randint(0, 100000000),
        'salary': random.randint(30000000, 150000000),
    }
    users.append(user)

# 상품 데이터 생성
with open('savings.json', 'r', encoding='utf-8') as f:
    savings_data = json.load(f)

# 'depositproducts'와 'savingproducts' 데이터를 추출
savings_products = [item for item in savings_data if item['model'] == 'savings.depositproducts'] + [item for item in savings_data if item['model'] == 'savings.savingproducts']


for i in range(N):
    num = random.sample(range(1, len(savings_products)), M)
    for j in range(M):
        product = savings_products[num[j]]
        if product['model'] == 'savings.depositproducts':
            prdt_type = 'deposit'
        elif product['model'] == 'savings.savingproducts':
            prdt_type = 'saving'

        product_dict = OrderedDict()
        product_dict['model'] = 'accounts.product'
        product_dict['pk'] = i * M + j + 1
        product_dict['fields'] = {
            'user': i+1,
            'prdt_type': prdt_type,
            'fin_prdt_cd': product['fields']['fin_prdt_cd'],
            'fin_prdt_nm': product['fields']['fin_prdt_nm'],
            'kor_co_nm': product['fields']['kor_co_nm'],
        }
        products.append(product_dict)


# JSON 파일로 저장
save_dir = 'accounts.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    json.dump(users + products, f, ensure_ascii=False, indent=4)

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
