<template>
  <div class="d-flex justify-content-between align-items-center mb-4">
    <div class="search-form">
      <label for="selectBank" class="form-label">은행선택</label>
      <select
        id="selectBank"
        v-model="selectedBank"
        @change="fetchProducts"
        class="form-select"
      >
        <option
          v-for="bank in store.bankList"
          :key="bank.fin_co_no"
          :value="bank.fin_co_no"
        >
          {{ bank.kor_co_nm }}
        </option>
      </select>
    </div>
    <div class="card p-3 sort-card" style="max-width: 400px">
      <div class="d-flex justify-content-between align-items-center">
        <div
          :class="['sort-option', { selected: isBestSort }]"
          @click="sortByMaxInterest"
        >
          최대 금리순
        </div>
        <div
          :class="['sort-option', { selected: !isBestSort }]"
          @click="sortByBaseInterest"
        >
          기본 금리순
        </div>
      </div>
    </div>
  </div>

  <div>
    <!-- 은행 select했을 때 if문 -->
    <div v-if="products.length">
      <!-- 최대 금리순 -->
      <div v-if="isBestSort">
        <div
          v-for="item in products"
          :key="item.fin_prdt_cd"
          class="card m-3 custom-card"
          @click="goDetailPage(item.fin_prdt_cd)"
        >
          <div class="card-body row">
            <div class="col-9">
              <h4>{{ item.fin_prdt_nm }}</h4>
              <p>{{ item.kor_co_nm }}</p>
            </div>
            <div class="col-3 text-end">
              <p class="fw-bold mb-2 best">
                최고
                {{ item.max_after }}%
              </p>
              <p>
                기본
                {{ item.max_before }}%
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- 기본 금리순 -->
      <div v-else>
        <div
          v-for="item in products.toSorted(function (a, b) {
            return b.max_before - a.max_before;
          })"
          :key="item.fin_prdt_cd"
          class="card m-3 custom-card"
          @click="goDetailPage(item.fin_prdt_cd)"
        >
          <div class="card-body row">
            <div class="col-9">
              <h4>{{ item.fin_prdt_nm }}</h4>
              <p>{{ item.kor_co_nm }}</p>
            </div>
            <div class="col-3 text-end">
              <p class="fw-bold mb-2 best">
                최고
                {{ item.max_after }}%
              </p>
              <p>
                기본
                {{ item.max_before }}%
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 은행 select 안했을 때 -->
    <div v-else>
      <!-- 최대 금리순 정렬 -->
      <div class="sortProducts" v-if="isBestSort">
        <div
          v-for="item in store.depositList"
          :key="item.fin_prdt_cd"
          class="card m-3 custom-card"
          @click="goDetailPage(item.fin_prdt_cd)"
        >
          <div class="card-body row">
            <div class="col-9">
              <h4>{{ item.fin_prdt_nm }}</h4>
              <p>{{ item.kor_co_nm }}</p>
            </div>
            <div class="col-3 text-end">
              <p class="fw-bold mb-2 best">
                최고
                {{ item.max_after }}%
              </p>
              <p>
                기본
                {{ item.max_before }}%
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- 기본 금리순 정렬 -->
      <div class="sortProducts" v-if="!isBestSort">
        <div
          v-for="item in store.depositNormalList"
          :key="item.fin_prdt_cd"
          class="card m-3 custom-card"
          @click="goDetailPage(item.fin_prdt_cd)"
        >
          <div class="card-body row">
            <div class="col-9">
              <h4>{{ item.fin_prdt_nm }}</h4>
              <p>{{ item.kor_co_nm }}</p>
            </div>
            <div class="col-3 text-end">
              <p class="fw-bold mb-2 best">
                최고
                {{ item.max_after }}%
              </p>
              <p>
                기본
                {{ item.max_before }}%
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from "@/stores/saving";
import { useUserStore } from "@/stores/user";
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useBankStore();
const router = useRouter();
const userStore = useUserStore();

// 은행 검색 사용
const selectedBank = ref("");
const products = ref([]);

const fetchProducts = function () {
  if (selectedBank.value) {
    axios({
      method: "get",
      url: `${store.API_URL}/savings/deposit-bank/${selectedBank.value}`,
    })
      .then((response) => {
        console.log(selectedBank.value);
        products.value = response.data;
        console.log(response.data);
      })
      .catch((err) => console.log(err));
  } else {
    products.value = [];
  }
};

// 최고금리순, 기본금리순 정렬
const isBestSort = ref(true);

const sortByMaxInterest = function () {
  isBestSort.value = true;
};
const sortByBaseInterest = function () {
  isBestSort.value = false;
};

// detail 페이지로 이동
const goDetailPage = function (fin_prdt_cd) {
  if (!userStore.isLogin) {
    const check = confirm("로그인 후 조회 가능합니다.");
    if (check) {
      router.push({ name: "logIn" });
    }
  } else {
    router.push({
      name: "depositDetail",
      params: { fin_prdt_cd: fin_prdt_cd },
    });
  }
};
</script>

<style scoped>
.custom-card {
  cursor: pointer;
  transition: background-color 0.3s, border-color 0.3s;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.custom-card:hover {
  background-color: #f8f9fa; /* 배경색 */
  border-color: #1b3074; /* 테두리 색 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 약간의 그림자 효과 추가 */
}

.sort-card {
  border: 0;
}

.sort-option {
  padding: 10px 20px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.sort-option.selected {
  background-color: #1b3074;
  color: white;
  border-radius: 5px;
}

.sort-option:not(.selected) {
  color: #d3d3d1;
}

.sort-option:hover:not(.selected) {
  background-color: #e6e6e3;
  color: black;
  border-radius: 5px;
}

.best {
  font-size: large;
  color: #1b3074;
}
</style>
