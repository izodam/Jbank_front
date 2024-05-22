<template>
  <div class="container text-center mt-4">
    <h2>COMMUNITY</h2>
    <ArticleList class="text-start" />
  </div>
</template>

<script setup>
import ArticleList from "@/components/ArticleList.vue";
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/article";
import { useUserStore } from "@/stores/user";

const store = useArticleStore();
const userStore = useUserStore();

console.log(userStore.token);
onMounted(() => {
  store.getArticles(userStore.token);
});
</script>

<style lang="scss" scoped></style>
