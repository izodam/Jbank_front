<template>
  <div>
    <h1>Detail</h1>
    <div v-if="store.articleDetail.length !== 0">
      <p>글 번호: {{ store.articleDetail.article.id }}</p>
      <p>제목: {{ store.articleDetail.article.title }}</p>
      <p>내용: {{ store.articleDetail.article.content }}</p>
      <p>작성날짜: {{ store.articleDetail.article.created_at }}</p>
      <p>수정날짜: {{ store.articleDetail.article.updated_at }}</p>
      <div class="comment">
        <h5>댓글</h5>
        <div v-if="store.articleDetail.comments.length">
          <div v-for="comment in store.articleDetail.comments">
            <p>{{ comment.user }} - {{ comment.content }}</p>
          </div>
        </div>
        <div>
          <form @submit.prevent="createComment">
            <label for="comment"></label>
            <input type="text" id="comment" v-model="commentContent" />
            <input type="submit" />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useArticleStore } from "@/stores/article";
import { useUserStore } from "@/stores/user";

const store = useArticleStore();
const userStore = useUserStore();
const route = useRoute();
const articleDetail = ref(null);
const article = ref(null);
const comments = ref([]);

const commentContent = ref("");

const createComment = function () {
  axios({
    method: "post",
    url: `${userStore.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      content: commentContent.value,
    },
  })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => console.log(err));
};

onMounted(() => {
  store.getDetail(userStore.token, route.params.id);
});
</script>

<style scoped></style>
