<template>
  <div class="mt-5">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">No.</th>
          <th scope="col">제목</th>
          <th scope="col">글쓴이</th>
          <th scope="col">작성시간</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="article in store.articles"
          :key="article.id"
          @click="goToDetail(article.id)"
        >
          <th scope="row">{{ article.id }}</th>
          <td>{{ article.title }}</td>
          <td>{{ article.user }}</td>
          <td>{{ article.created_at }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { useRouter } from "vue-router";

const store = useArticleStore();
const router = useRouter();

const goToDetail = function (id) {
  router.push({ name: "articleDetail", params: { id: id } });
};
</script>

<style lang="scss" scoped></style>
