<template>
  <div class="container mt-4">
    <div class="row" v-if="store.hotProduct">
      <h4 class="mb-4">놓치지 마세요! 현재 Hot한 상품</h4>
      <div class="col-5">
        <table class="table table-hover">
          <thead class="table-light">
            <tr>
              <th scope="col"></th>
              <th scope="col" class="no-wrap">상품명</th>
              <th scope="col" class="no-wrap">은행</th>
              <th scope="col" class="text-end">금리</th>
              <th scope="col" class="text-end">현재 가입자수</th>
              <th scope="col" class="text-end"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(product, idx) in store.hotProduct.products"
              :key="product.fin_prdt_cd"
            >
              <td>{{ idx + 1 }}</td>
              <td>{{ product.fin_prdt_nm }}</td>
              <td>{{ product.kor_co_nm }}</td>
              <td class="text-end">{{ product.max_after }} %</td>
              <td class="text-end">{{ product.user_count }}명</td>
              <td class="text-end"></td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-7">
        <div class="card custom-card">
          <div class="card-header fw-bold">금리 비교</div>
          <!-- <h3>가입한 상품 금리</h3> -->
          <img
            :src="'data:image/png;base64,' + store.hotProduct.chart"
            alt="chart"
            class="card-body"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { useBankStore } from "@/stores/saving";

const userStore = useUserStore();
const store = useBankStore();
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
}
.card-header {
  background-color: #f7f7f7;
}
.card-body {
  background-color: #fff;
}
.card-footer {
  background-color: #f7f7f7;
}
table {
  height: 100%;
}
.no-wrap {
  /* font-size: 12px; Adjust the size as necessary */
  white-space: nowrap;
}
</style>
