<template>
  <div class="container mt-5">
    <h3>{{ userStore.nowUserName }}님!</h3>
    <div class="card mt-4">
      <div class="card-body">
        <h5>기본 정보</h5>
        <hr />
        <p>이름 : {{ userStore.myProduct.user.username }}</p>
        <p>나이 : {{ userStore.myProduct.user.age }}</p>
        <p>자산 : {{ userStore.myProduct.user.money }}</p>
        <p>연봉 : {{ userStore.myProduct.user.salary }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
console.log(userStore.myProduct);
</script>

<style lang="scss" scoped></style>
