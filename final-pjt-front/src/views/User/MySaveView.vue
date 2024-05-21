<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4" v-if="userStore.myProduct">
      {{ userStore.myProduct.user.username }}님의 가입 상품
    </h1>
    <table
      v-if="userStore.myProduct.products.length !== 0"
      class="table table-hover"
    >
      <thead class="table-light">
        <tr>
          <th scope="col"></th>
          <th scope="col">상품명</th>
          <th scope="col">종류</th>
          <th scope="col" class="text-end">최대금리</th>
          <th scope="col" class="text-end"></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(product, idx) in userStore.myProduct.products"
          :key="product.fin_prdt_cd"
        >
          <td>{{ idx + 1 }}</td>
          <td>{{ product.fin_prdt_nm }}</td>
          <td>{{ savingOrDeposit[product.prdt_type] }}</td>
          <td class="text-end">{{ product.max_after }} %</td>
          <td class="text-end">
            <button
              class="btn btn-outline-danger btn-sm btn-sm"
              @click="cancelSubscription(product)"
            >
              가입 취소하기
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <table v-else class="table table-hover">
      <thead class="table-light">
        <tr>
          <th scope="col">상품명</th>
          <th scope="col" class="text-end"></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>가입된 상품이 없습니다.</td>
          <td class="text-end">
            <button
              class="btn btn-outline-primary btn-sm me-2"
              @click="goSavings"
            >
              상품 보러가기
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const router = useRouter();

const savingOrDeposit = { saving: "적금", deposit: "예금" };

const goSavings = function () {
  router.push({ name: "compareSaving" });
};

const cancelSubscription = function (product) {
  axios({
    method: "post",
    url: `${userStore.API_URL}/accounts/cancel-product/`,
    data: {
      prdt_type: product.prdt_type,
      fin_prdt_cd: product.fin_prdt_cd,
    },
    headers: { Authorization: `Token ${userStore.token}` },
  })
    .then((res) => {
      // console.log(res.data);
      axios({
        method: "get",
        url: `${userStore.API_URL}/accounts/profile/`,
        headers: { Authorization: `Token ${userStore.token}` },
      })
        .then((res) => {
          // console.log(res.data);
          userStore.myProduct = res.data;
        })
        .catch((err) => console.log(err));
    })
    .catch((err) => console.log(err));
};

onMounted(() => {
  userStore.findMyProduct();
});
</script>

<style scoped>
.container {
  max-width: 960px;
}
.table {
  background-color: #ffffff;
  border-radius: 10px;
  overflow: hidden;
}
.table th,
.table td {
  vertical-align: middle;
}
.table-hover tbody tr:hover {
  background-color: #f1f1f1;
}

.btn {
  border-radius: 20px;
}
.btn-outline-primary {
  color: #1b3074;
  border-color: #1b3074;
}
.btn-outline-primary:hover {
  background-color: #1b3074;
  color: white;
}
.btn-outline-danger {
  color: #bb243c;
  border-color: #bb243c;
}
.btn-outline-danger:hover {
  background-color: #bb243c;
  color: white;
}
</style>
