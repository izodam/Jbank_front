<template>
  <div class="mt-3">
    <div class="mb-3 ms-auto">
      <button class="btn btn-light write-btn">
        <RouterLink :to="{ name: 'articleCreate' }"> 글쓰기 </RouterLink>
      </button>
    </div>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">No.</th>
          <th scope="col">제목</th>
          <th scope="col" class="text-end">글쓴이</th>
          <th scope="col" class="text-end">작성날짜</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(article, idx) in store.articles"
          :key="article.id"
          @click="goToDetail(article.id)"
        >
          <th scope="row">{{ idx + 1 }}</th>
          <td>{{ article.title }}</td>
          <td class="text-end">{{ article.nickname }}</td>
          <td class="text-end created-at">
            {{ article.created_at.substring(0, 10) }}
          </td>
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

<style scoped>
.created-at {
  color: gray;
  font-size: small;
}

.write-btn {
  background-color: #dad9d9;
  border-color: #dad9d9;
}

a {
  color: black;
  text-decoration-line: none;
}
</style>
