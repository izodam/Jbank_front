<template>
  <div class="">
    <div class="create-box mt-3">
      <button class="mb-3 ps-0 back-btn" @click="goToBack">
        <span class="material-symbols-outlined">arrow_back</span>
      </button>
      <h3 class="mt-1">글쓰기</h3>
      <form @submit.prevent="createArticle" class="article-form">
        <div class="form-group">
          <label for="title">제목 :</label>
          <input
            type="text"
            id="title"
            v-model.trim="title"
            class="form-control w-100"
            placeholder="제목을 입력하세요"
          />
        </div>
        <div class="form-group">
          <label for="content">내용 :</label>
          <textarea
            id="content"
            v-model.trim="content"
            class="form-control"
            placeholder="내용을 입력하세요"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">작성</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useUserStore();

const title = ref(null);
const content = ref(null);

const createArticle = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      router.push({ name: "article" });
    })
    .catch((err) => console.log(err));
};

const goToBack = function () {
  router.push({ name: "article" });
};
</script>

<style scoped>
.create-box {
  max-width: 600px;
  height: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h3 {
  color: #333;
  margin-bottom: 20px;
}

.article-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group > textarea {
  height: 230px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
  display: inline-block;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  border-color: #e6e6e3;
}

.form-control:focus {
  border-color: #1b3074;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.btn {
  padding: 10px 15px;
  font-size: 16px;
  color: #fff;
  background-color: #25419b;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}

.back-btn {
  background-color: #f9f9f9;
  border: 0px;
  margin-bottom: 2%;
}
</style>
