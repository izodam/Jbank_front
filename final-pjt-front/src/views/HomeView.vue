<template>
  <div class="home-page">
    <div
      id="carouselExampleControls"
      class="carousel slide"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <div
          v-for="(item, index) in carouselItems"
          :key="index"
          :class="['carousel-item', { active: index === 0 }]"
        >
          <div
            :style="{
              'background-color': item.backgroundColor,
              color: item.color,
            }"
            class="d-block w-100 carousel-content text-start"
          >
            <h1>{{ item.title }}</h1>
            <p>{{ item.description }}</p>
            <router-link
              :to="item.buttonLink"
              class="btn btn-primary"
              :style="{
                'background-color': item.buttonColor,
                'border-color': item.buttonColor,
                color: item.buttonTextColor,
              }"
              >{{ item.buttonText }}</router-link
            >
          </div>
        </div>
      </div>
      <button
        class="carousel-control-prev control-btn"
        type="button"
        data-bs-target="#carouselExampleControls"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next control-btn"
        type="button"
        data-bs-target="#carouselExampleControls"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <Hotproduct />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { useBankStore } from "@/stores/saving";
import Hotproduct from "@/components/Hotproduct.vue";

const userStore = useUserStore();
const store = useBankStore();

const carouselItems = ref([
  {
    title: "상품 추천",
    description: "회원님의 정보를 바탕으로 예적금을 추천해줍니다!!",
    buttonLink: "/compareSaving/recommend",
    buttonText: "추천 받으러 가기",
    buttonColor: "#3D4856",
    backgroundColor: "#A8C2E5",
    color: "black",
  },
  {
    title: "환율 계산",
    description: "국가별 환율을 한눈에! 환율 계산기까지 제공합니다",
    buttonLink: "/exchange",
    buttonText: "계산기 사용하기",
    buttonColor: "#4A5F6B",
    backgroundColor: "#A5B8C4",
    color: "black",
  },
  {
    title: "예적금 조회",
    description: "은행 별 예금과 적금을 금리 순으로 정렬해 비교해줍니다!",
    buttonLink: "/compareSaving",
    buttonText: "비교해보러 가기",
    buttonColor: "#4F7C95",
    backgroundColor: "#84B1CB",
    color: "black",
  },
  {
    title: "은행 찾기",
    description:
      "지역별 은행을 찾아줍니다. 검색해서 바로 예적금 가입하러 가면 되겠죠?",
    buttonLink: "/map",
    buttonText: "검색하러 가요",
    buttonColor: "rgb(234, 232, 232)",
    buttonTextColor: "black",
    backgroundColor: "#4E616D",
  },
]);

const savingOrDeposit = { saving: "적금", deposit: "예금" };

onMounted(() => {
  new bootstrap.Carousel(document.getElementById("carouselExampleControls"), {
    interval: 3000, // 원하는 간격으로 설정하세요.
  });
  axios({
    method: "get",
    url: `${userStore.API_URL}/accounts/hot-products/`,
    // headers: {
    //   Authorization: `Token ${token}`,
    // },
  })
    .then((response) => {
      console.log(response.data);
      store.hotProduct = response.data;
    })
    .catch((err) => console.log(err));
});

console.log(userStore.myProduct);
</script>

<style scoped>
.carousel-content {
  color: rgb(234, 232, 232);
  text-align: left;
  padding: 70px;
  padding-left: 70px;
}
.control-btn {
  width: 50px;
}
</style>
