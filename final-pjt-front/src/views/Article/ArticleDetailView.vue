<template>
  <div class="container">
    <button class="btn mb-3 ps-0 back-btn" @click="goToBack">
      <span class="material-symbols-outlined">arrow_back</span>
    </button>
    <div class="header" v-if="store.articleDetail.length !== 0">
      <h3>{{ store.articleDetail.article.title }}</h3>
      <div>
        <button
          v-if="store.articleDetail.article.nickname == userStore.nowUserName"
          @click="updateArticle"
          class="btn btn-primary update-btn me-2"
        >
          수정하기
        </button>
        <button
          v-if="store.articleDetail.article.nickname == userStore.nowUserName"
          @click="deleteArticle"
          class="btn btn-primary update-btn"
        >
          삭제하기
        </button>
      </div>
    </div>
    <div v-if="store.articleDetail.length !== 0" class="article-details pt-0">
      <p class="meta">
        <span class="author">{{ store.articleDetail.article.nickname }}</span>
        <span class="date">{{
          store.articleDetail.article.created_at.substring(0, 10)
        }}</span>
      </p>
      <p class="content mt-4">{{ store.articleDetail.article.content }}</p>
      <div class="comment-section">
        <h5>댓글</h5>
        <div v-if="store.articleDetail.comments.length">
          <div
            v-for="comment in store.articleDetail.comments"
            :key="comment.id"
            :class="['comment-item', { expanded: showOptions === comment.id }]"
          >
            <div v-if="editingCommentId !== comment.id" class="">
              <div class="comment-content w-100">
                <h5>{{ comment.nickname }}</h5>
                <i
                  v-if="comment.nickname == userStore.nowUserName"
                  @click="toggleOptions(comment.id)"
                  class="options-toggle fas fa-ellipsis-h ms-auto"
                ></i>
              </div>
              <div v-if="showOptions === comment.id" class="options">
                <span @click="commentUpdate(comment.id, comment.content)"
                  >수정</span
                >
                <span @click="deleteComment(comment.id)">삭제</span>
              </div>
              <p>{{ comment.content }}</p>
              <p class="meta mt-3">{{ comment.updated_at.substring(0, 10) }}</p>
            </div>
            <form
              v-else
              @submit.prevent="updateComment(comment.id)"
              class="edit-comment-form"
            >
              <input
                type="text"
                v-model="updateCommentContent"
                class="form-control"
              />
              <button
                type="submit"
                class="btn btn-secondary update-comment-btn"
              >
                수정
              </button>
            </form>
          </div>
        </div>
        <div class="add-comment">
          <form @submit.prevent="createComment">
            <label for="comment">댓글 추가</label>
            <input
              type="text"
              id="comment"
              v-model="commentContent"
              class="form-control"
            />
            <button type="submit" class="btn btn-primary comment-btn">
              작성
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useArticleStore } from "@/stores/article";
import { useUserStore } from "@/stores/user";

const store = useArticleStore();
const userStore = useUserStore();
const route = useRoute();
const router = useRouter();
const editingCommentId = ref(null);
const updateCommentContent = ref("");
const commentContent = ref("");
const showOptions = ref(null);

console.log(userStore.nowUserName);
const createComment = function () {
  if (commentContent.value === "") {
    confirm("입력해주세요!");
  } else {
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
        store.getDetail(userStore.token, route.params.id);
        commentContent.value = "";
      })
      .catch((err) => console.log(err));
  }
};

const updateArticle = function () {
  router.push({
    name: "articleUpdate",
    params: {
      id: route.params.id,
    },
  });
};

const commentUpdate = function (id, content) {
  editingCommentId.value = id;
  updateCommentContent.value = content;
};

const updateComment = function (id) {
  axios({
    method: "put",
    url: `${userStore.API_URL}/api/v1/articles/${route.params.id}/comment/${id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      content: updateCommentContent.value,
    },
  })
    .then((res) => {
      editingCommentId.value = null;
      store.getDetail(userStore.token, route.params.id);
    })
    .catch((err) => console.log(err));
};

const deleteComment = function (id) {
  axios({
    method: "delete",
    url: `${userStore.API_URL}/api/v1/articles/${route.params.id}/comment/${id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      store.getDetail(userStore.token, route.params.id);
    })
    .catch((err) => console.log(err));
};

const toggleOptions = function (id) {
  showOptions.value = showOptions.value === id ? null : id;
};
const goToBack = function () {
  router.push({ name: "article" });
};

const deleteArticle = function () {
  axios({
    method: "delete",
    url: `${userStore.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log("삭제 완료");
      router.push({ name: "article" });
    })
    .catch((err) => console.log(err));
};

onMounted(() => {
  store.getDetail(userStore.token, route.params.id);
});
</script>

<style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css");

.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 40px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #e5e7eb;
  padding-bottom: 10px;
}

.header h1 {
  font-size: 2.5em;
  color: #333;
  margin: 0;
}

.article-details {
  padding: 20px 0;
}

.meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  margin-top: 0px;
  color: #777;
}

.content {
  margin-bottom: 20px;
  line-height: 1.6;
}

.btn {
  padding: 8px 16px;
  font-size: 14px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary {
  background-color: #007bff;
  color: white;
  border: none;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
  border: none;
}

.btn-secondary:hover {
  background-color: #5a6268;
}

.btn-success {
  background-color: #28a745;
  color: white;
  border: none;
}

.btn-success:hover {
  background-color: #218838;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
  border: none;
}

.btn-danger:hover {
  background-color: #c82333;
}

.comment-section {
  margin-top: 30px;
}

.comment-item {
  width: 100%;
  min-height: 120px;
  padding: 15px;
  border-bottom: 1px solid #e5e7eb;
  /* display: flex; */
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.comment-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.comment-item p {
  margin: 0;
  flex: 1;
}

.comment-item i.options-toggle {
  cursor: pointer;
  color: #6c757d;

  transition: color 0.3s ease;
}

.comment-item i.options-toggle:hover {
  color: #333;
}

.options {
  position: absolute;
  /* margin-left: auto; */
  right: 0;
  width: 10%;
  background: white;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 5px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  z-index: 10;
}

.options span {
  cursor: pointer;
  color: #1b3074;
  transition: color 0.3s ease;
}

.options span:hover {
  color: #5d5f65;
}

.edit-comment-form {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}

.edit-comment-form .form-control {
  flex: 1;
}

.add-comment {
  margin-top: 20px;
}

.form-control {
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}

.form-control:focus {
  border-color: #007bff;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

.comment-btn {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #1b3074;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.comment-btn:hover {
  background-color: #1b3074;
}

.update-btn {
  background-color: #1b3074;
}

.update-comment-btn {
  background-color: #555;
}

.update-comment-btn:hover {
  background-color: #555;
}
</style>
