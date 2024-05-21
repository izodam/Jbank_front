<template>
  <div class="mt-0">
    <nav class="navbar mb-3">
      <div class="container-fluid">
        <ul class="nav nav-underline me-auto">
          <li class="nav-item align-self-end mx-2">
            <RouterLink
              class="nav-link link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover"
              :to="{ name: 'deposit' }"
            >
              정기예금
            </RouterLink>
          </li>
          <li class="nav-item align-self-end mx-2">
            <RouterLink
              class="nav-link link-body-emphasis link-offset-2"
              :to="{ name: 'saving' }"
            >
              정기적금
            </RouterLink>
          </li>
          <li class="nav-item align-self-end mx-2">
            <RouterLink
              class="nav-link link-body-emphasis link-offset-2"
              :to="{ name: 'freeSaving' }"
            >
              자유적금
            </RouterLink>
          </li>
          <li class="nav-item align-self-end mx-2">
            <RouterLink
              class="nav-link link-body-emphasis link-offset-2"
              :to="{ name: 'recommend' }"
            >
              상품 추천받기
            </RouterLink>
          </li>
        </ul>
      </div>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.navbar {
  background-color: #e6e6e3;
}
</style>
