<template>
  <div class="container">
    <button class="btn mb-3 ps-0 back-btn" @click="goToBack">
      <span class="material-symbols-outlined">arrow_back</span>
    </button>
  </div>
  <div v-if="store.depositDetail.length === 0">loading</div>
  <div v-else class="container">
    <div class="row">
      <div class="first-detail col-10">
        <h4>{{ store.depositDetail.kor_co_nm }}</h4>
        <h4 class="mb-5">{{ store.depositDetail.fin_prdt_nm }}</h4>
      </div>
      <div class="col-2 text-end">
        <div v-if="userStore.isLogin">
          <button v-if="store.isJoin" class="btn btn-primary cancle-btn" @click="changeCancle">가입취소</button>
          <button v-else class="btn btn-primary join-btn" @click="changeJoin">가입하기</button>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-2">
        <p class="mb-1">최고 금리</p>
        <p>{{ store.depositDetail["12month_after"] }}</p>
      </div>
      <div class="col-2">
        <p class="mb-1">기본 금리</p>
        <p>{{ store.depositDetail["12month_before"] }}</p>
      </div>
    </div>
    <hr />

    <div class="month-calcul">
      <h3>이자 계산기</h3>
      <div class="button-container">
        <div class="btn-group" role="group">
          <button
            v-for="(label, key) in filteredButtons"
            :key="key"
            @click="selectMonth(label)"
            class="custom-button"
          >
            {{ buttons[label] }}
          </button>
        </div>
      </div>
      <div class="mt-3" v-if="selectedMonth">
        <h3>{{ buttons[selectedMonth] }} 후 금액</h3>
        <p>{{ store.depositDetail[selectedMonth] }}%</p>
        <p>1000만원 기준</p>
        <p>세후 이자 {{ store.money.toLocaleString("ko-KR") }}원</p>
      </div>
      <div v-else>
        <p>개월수를 선택해주세요</p>
      </div>
    </div>
    <hr />

    <div class="detail">
      <p>만기후 이자율 : <p v-html="formattedInterestRate"></p></p>
      <p>가입 방법 : {{ store.depositDetail["join_way"] }}</p>
      <p>가입 대상 : {{ store.depositDetail["join_member"] }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useBankStore } from "@/stores/saving";
import { useUserStore } from "@/stores/user";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const store = useBankStore();
const userStore = useUserStore()
const route = useRoute();
const router = useRouter()
const fin_prdt_cd = route.params.fin_prdt_cd;

const buttons = {
  "1month_after": "1개월",
  "3month_after": "3개월",
  "6month_after": "6개월",
  "12month_after": "12개월",
  "24month_after": "24개월",
  "36month_after": "36개월",
};

const formattedInterestRate = computed(() => {
  const interestRate = store.depositDetail["mtrt_int"];
  if (interestRate) {
    return interestRate.replace(/\n/g, "<br>");
  }
  return "";
});

const filteredButtons = computed(() => {
  return Object.keys(buttons).filter((key) => store.depositDetail[key] !== 0.0);
});

const selectedMonth = ref(null);
const selectMonth = function (label) {
  const regex = /[^0-9]/g;
  const res = label.replace(regex, "");
  const month = parseInt(res);

  selectedMonth.value = label;
  store.money =
    10000000 *
    store.depositDetail[selectedMonth.value] *
    0.01 *
    0.846 *
    (month / 12);
};

onMounted(() => {
  store.findDetail(fin_prdt_cd, userStore.token);
});

const goToBack = function () {
  router.push({name: 'deposit'})
}

const changeJoin = function() {
  const check = confirm('가입하시겠습니까?')
  if (check){
    axios({
      method: "post",
      url: `${store.API_URL}/accounts/join-product/`,
      headers: {'Authorization': `Token ${userStore.token}`},
      data: {
        prdt_type: 'deposit',
        fin_prdt_cd: fin_prdt_cd
      }
    })
    .then(res => {
      store.findDetail(fin_prdt_cd, userStore.token);
    }) 
    .catch(err => console.log(err))
  }
}
const changeCancle = function () {
  const check = confirm('정말 취소하시겠습니까?')
  if (check)
  {axios({
    method: "post",
    url: `${store.API_URL}/accounts/cancel-product/`,
    data: {
      prdt_type: 'deposit',
      fin_prdt_cd: fin_prdt_cd
    },
    headers: {'Authorization': `Token ${userStore.token}`},
  })
  .then(res => {
    store.findDetail(fin_prdt_cd, userStore.token);
  }) 
  .catch(err => console.log(err))}
}
</script>

<style scoped>
.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.btn-group {
  display: flex;
  gap: 10px;
}

.custom-button {
  padding: 10px;
  border-radius: 10px;
  width: 100px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  cursor: pointer;
  transition: background-color 0.3s;
}

.custom-button:hover {
  background-color: #e0e0e0;
}

.custom-button:focus {
  outline: none;
  box-shadow: 0 0 0 2px #1b3074;
}
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 24
}

.join-btn {
  background-color: #1b3074;
  height: 60px;
}

.join-btn:hover{
  background-color: #e6e6e3;
  color: black;
  border-color: #e6e6e3;
}
.cancle-btn {
  background-color: #e6e6e3;
  color: black;
  height: 60px;
  border-color: #e6e6e3;
}

.cancle-btn:hover{
  background-color: #ac4747;
  color: white;
  border-color: #ac4747;

}

.back-btn {
  border: 0px;
}
</style>
