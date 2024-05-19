<template>
  <div>
    <h1>정기예금</h1>
    <div class="search-form">
      <select v-model="selectedBank" @change="fetchProducts">
        <option v-for="bank in bankList" :key="bank">{{ bank }}</option>
      </select>
    </div>
    <div v-if="products.length">
      <h2>{{ selectedBank }}의 상품 목록</h2>
      <div
        v-for="item in products"
        :key="item.fin_prdt_cd"
        class="card m-3 custom-card"
        @click="goDetailPage(item.fin_prdt_cd)"
      >
        <div class="card-body row">
          <div class="col-9">
            <h4>{{ item.kor_co_nm }}</h4>
            <p>{{ item.fin_prdt_nm }}</p>
          </div>
          <div class="col-3 text-end">
            <p>
              최고
              {{ maxRate(item) }}%
            </p>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div
        v-for="item in depositList"
        :key="item.fin_prdt_cd"
        class="card m-3 custom-card"
        @click="goDetailPage(item.fin_prdt_cd)"
      >
        <div class="card-body row">
          <div class="col-9">
            <h4>{{ item.kor_co_nm }}</h4>
            <p>{{ item.fin_prdt_nm }}</p>
          </div>
          <div class="col-3 text-end">
            <p>
              최고
              {{ maxRate(item) }}%
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from "@/stores/saving";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useBankStore();
const router = useRouter();

// axios 요청 받아서 채워질 list들
const depositList = store.depositList;
const bankList = store.bankList;

// 은행 검색 사용
const selectedBank = ref(null);
const products = ref([]);

const fetchProducts = function () {
  if (selectedBank.value) {
    products.value = [
      {
        id: 1,
        dcls_month: "202404",
        fin_co_no: "0010001",
        fin_prdt_cd: "WR0001B",
        kor_co_nm: "우리은행",
        fin_prdt_nm: "WON플러스예금",
        join_way: "인터넷,스마트폰,전화(텔레뱅킹)",
        mtrt_int:
          "만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리",
        spcl_cnd: "해당사항 없음",
        join_deny: 1,
        join_member: "실명의 개인",
        etc_note:
          "- 가입기간: 1~36개월\n- 최소가입금액: 1만원 이상\n- 만기일을 일,월 단위로 자유롭게 선택 가능\n- 만기해지 시 신규일 당시 영업점과 인터넷 홈페이지에 고시된 계약기간별 금리 적용",
        max_limit: null,
        dcls_strt_day: "20240424",
        dcls_end_day: null,
        fin_co_subm_day: "202404240919",
        "6month_before": 2.0,
        "6month_after": 3.0,
        "12month_before": 2.2,
        "12month_after": 3.2,
        "24month_before": 2.4,
        "24month_after": 3.4,
        "36month_before": 2.6,
        "36month_after": 3.6,
      },
    ];
    // axios({
    //   method: "get",
    //   url: `${store.API_URL}/`,
    // })
    //   .then((response) => {
    //     products.value = response.data;
    //   })
    //   .catch((err) => console.log(err));
  } else {
    products.value = [];
  }
};

// 최대 rate 출력할 함수
const maxRate = function (item) {
  return Math.max(
    item["6month_before"],
    item["12month_before"],
    item["24month_before"],
    item["36month_before"]
  );
};

// detail 페이지로 이동
const goDetailPage = function (fin_prdt_cd) {
  router.push({ name: "depositDetail", params: { fin_prdt_cd: fin_prdt_cd } });
};

onMounted(() => {
  store.fillDepositList;
});
</script>

<style scoped>
.custom-card {
  cursor: pointer;
  transition: background-color 0.3s, border-color 0.3s;
}

.custom-card:hover {
  background-color: #f8f9fa; /* 배경색 */
  border-color: #007bff; /* 테두리 색 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 약간의 그림자 효과 추가 */
}
</style>
