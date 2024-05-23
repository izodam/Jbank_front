// 유저 정보 저장할 store
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import axios from "axios";

export const useArticleStore = defineStore("article", () => {
  // const articles = ref([
  //   {
  //     id: 1,
  //     title: "Article 1",
  //     content: "Content of article 1",
  //     user: "user1",
  //     created_at: "2024-05-21",
  //   },
  //   {
  //     id: 2,
  //     title: "Article 2",
  //     content: "Content of article 2",
  //     user: "user1",
  //     created_at: "2024-05-21",
  //   },
  //   {
  //     id: 3,
  //     title: "Article 3",
  //     content: "Content of article 3",
  //     user: "user1",
  //     created_at: "2024-05-21",
  //   },
  //   {
  //     id: 4,
  //     title: "Article 4",
  //     content: "Content of article 4",
  //     user: "user1",
  //     created_at: "2024-05-21",
  //   },
  //   {
  //     id: 5,
  //     title: "Article 5",
  //     content: "Content of article 5",
  //     user: "user1",
  //     created_at: "2024-05-21",
  //   },
  // ]);

  const articles = ref([]);
  const API_URL = "http://127.0.0.1:8000";
  const articleDetail = ref([]);

  const getArticles = function (token) {
    axios({
      method: "get",
      url: `${API_URL}/api/v1/articles/`,
      // headers: {
      //   Authorization: `Token ${token}`,
      // },
    })
      .then((res) => {
        console.log(res.data);
        articles.value = res.data;
        articleDetail.value = [];
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const getDetail = function (token, articleId) {
    axios({
      method: "get",
      url: `${API_URL}/api/v1/articles/${articleId}/`,
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        console.log(res.data);
        articleDetail.value = res.data;
      })
      .catch((err) => console.log(err));
  };

  return { articles, articleDetail, getArticles, getDetail };
});
