<template>
  <div class="container">
    <h2>정기예금</h2>

    <div
      v-if="store.depositList.length === 0"
      class="spinner-border"
      role="status"
    >
      <span class="visually-hidden">Loading...</span>
    </div>
    <div v-else>
      <depositList />
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from "@/stores/saving";
import { onMounted, ref } from "vue";
import axios from "axios";
import depositList from "@/components/DepositList.vue";

const store = useBankStore();

// 상품 리스트 axios 요청
onMounted(() => {
  store.depositDetail = [];

  if (store.depositList.length === 0) {
    axios({
      method: "get",
      url: `${store.API_URL}/savings/deposit-products`,
    })
      .then((response) => {
        store.depositList = response.data;

        store.depositNormalList = response.data.toSorted(function (a, b) {
          return b.max_before - a.max_before;
        });
        console.log(store.depositNormalList);
      })
      .catch((err) => console.log(err));
  }
});
</script>

<style scoped></style>
