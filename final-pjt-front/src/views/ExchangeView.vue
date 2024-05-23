<template>
  <div class="m-5">
    <!-- <h1>환율 계산 페이지</h1> -->
    <div v-if="exchange.length !== 0">
      <ExchangeArea :exchange="exchange" />
      <ExchangeTable :exchange="exchange" />
    </div>
    <div v-else>loading</div>
  </div>
</template>

<script setup>
import ExchangeTable from "@/components/ExchangeTable.vue";
import ExchangeArea from "@/components/ExchangeArea.vue";
import { useBankStore } from "@/stores/saving";
import { ref, onMounted } from "vue";
import axios from "axios";

// 환율 정보

const exchange = ref([]);

const store = useBankStore();

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/exchanges/`,
  })
    .then((response) => {
      console.log(response.data);
      exchange.value = response.data;
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped></style>
