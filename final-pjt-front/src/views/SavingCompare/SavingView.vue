<template>
  <div class="container">
    <h2>정기적금</h2>

    <div
      v-if="store.savingList.length === 0"
      class="spinner-border"
      role="status"
    >
      <span class="visually-hidden">Loading...</span>
    </div>
    <div v-else>
      <SavingList />
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from "@/stores/saving";
import { onMounted, ref } from "vue";
import axios from "axios";
import SavingList from "@/components/SavingList.vue";

const store = useBankStore();

// 상품 리스트 axios 요청
onMounted(() => {
  store.savingDetail = [];
  if (store.savingList.length === 0) {
    axios({
      method: "get",
      url: `${store.API_URL}/savings/saving-products`,
    })
      .then((response) => {
        store.savingList = response.data;

        store.savingNormalList = response.data.toSorted(function (a, b) {
          return b.max_before - a.max_before;
        });
      })
      .catch((err) => console.log(err));
  }
});
</script>

<style scoped></style>
