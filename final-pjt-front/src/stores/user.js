// 유저 정보 저장할 store
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import axios from "axios";

export const useUserStore = defineStore(
  "user",
  () => {
    const token = ref(null);
    const API_URL = "http://127.0.0.1:8000";
    const router = useRouter();
    const notUser = ref(false);
    const myProduct = ref([]);
    const nowUserName = ref("");
    const wrong = ref(false);

    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    const findMyProduct = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          // console.log(res.data);
          myProduct.value = res.data;
          nowUserName.value = res.data.user.nickname;
          if (nowUserName.value === null) {
            nowUserName.value = "Unknown";
          }
        })
        .catch((err) => console.log(err));
    };

    const signUp = function (payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          console.log("회원가입 완료");
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => {
          wrong.value = true;
          console.log(err);
        });
    };

    const logIn = function (payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          notUser.value = false;
          console.log("로그인 완료");
          console.log(res.data);
          token.value = res.data.key;
          findMyProduct();
          router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err);
          notUser.value = true;
        });
    };

    const logOut = function () {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          console.log("로그아웃 완료");
          console.log(res.data);
          token.value = null;
          router.push({ name: "home" });
        })
        .catch((err) => console.log(err));
    };

    return {
      nowUserName,
      token,
      wrong,
      API_URL,
      myProduct,
      isLogin,
      notUser,
      signUp,
      logIn,
      logOut,
      findMyProduct,
    };
  },
  { persist: true }
);
