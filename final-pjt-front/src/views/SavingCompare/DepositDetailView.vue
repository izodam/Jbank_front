<template>
  <div>
    <h1>상품 상세 페이지</h1>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useBankStore } from "@/stores/saving";
import { useRoute } from "vue-router";
import axios from "axios";

const store = useBankStore();
const depositList = store.depositList;

const route = useRoute();
const fin_prdt_cd = route.params.fin_prdt_cd;

const itemDetail = ref(null);

// onMounted(() => {
//   axios({
//     method: "get",
//     url: `${store.API_URL}/deposit-options/${fin_prdt_cd}/`,
//   })
//     .then((response) => {
//       itemDetail.value = response.data;
//     })
//     .catch((err) => console.log(err));
// });
</script>

<style lang="scss" scoped></style>
