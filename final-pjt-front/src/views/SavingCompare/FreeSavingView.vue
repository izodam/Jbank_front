<template>
  <div class="container">
    <h2>자유적금</h2>

    <div
      v-if="store.freeSavingList.length === 0"
      class="spinner-border"
      role="status"
    >
      <span class="visually-hidden">Loading...</span>
    </div>
    <div v-else>
      <FreeSavingList />
    </div>
  </div>
</template>

<script setup>
import { useBankStore } from "@/stores/saving";
import { onMounted, ref } from "vue";
import axios from "axios";
import FreeSavingList from "@/components/FreeSavingList.vue";

const store = useBankStore();

// 상품 리스트 axios 요청
onMounted(() => {
  store.freeSavingDetail = [];
  if (store.freeSavingList.length === 0) {
    axios({
      method: "get",
      url: `${store.API_URL}/savings/free-saving-products`,
    })
      .then((response) => {
        store.freeSavingList = response.data;

        store.freeSavingNormalList = response.data.toSorted(function (a, b) {
          return b.max_before - a.max_before;
        });
      })
      .catch((err) => console.log(err));
  }
});
</script>

<style scoped></style>
