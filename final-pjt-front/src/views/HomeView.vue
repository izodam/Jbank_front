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

    <div class="container mt-4">
      <div class="row">
        <h4 class="mb-4" v-if="userStore.myProduct">
          놓치지 마세요! 현재 Hot한 상품
        </h4>
        <div class="col-5">
          <table class="table table-hover">
            <thead class="table-light">
              <tr>
                <th scope="col"></th>
                <th scope="col" class="no-wrap">상품명</th>
                <th scope="col" class="no-wrap">은행</th>
                <th scope="col" class="text-end">금리</th>
                <th scope="col" class="text-end subscriber-count">
                  현재 가입자수
                </th>
                <th scope="col" class="text-end"></th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(product, idx) in store.hotProduct.products"
                :key="product.fin_prdt_cd"
              >
                <td>{{ idx + 1 }}</td>
                <td class="no-wrap">{{ product.fin_prdt_nm }}</td>
                <td class="no-wrap">{{ product.kor_co_nm }}</td>
                <td class="text-end no-wrap">{{ product.max_after }} %</td>
                <td class="text-end no-wrap">{{ product.user_count }}명</td>
                <td class="text-end"></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col-7">
          <div class="card custom-card">
            <div class="card-header fw-bold">금리 비교</div>
            <!-- <h3>가입한 상품 금리</h3> -->
            <img
              :src="'data:image/png;base64,' + store.hotProduct.chart"
              alt="chart"
              class="card-body"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { useBankStore } from "@/stores/saving";

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
.card {
  border: 1px solid #ddd;
}
.card-header {
  background-color: #f7f7f7;
}
.card-body {
  background-color: #fff;
}
.card-footer {
  background-color: #f7f7f7;
}
table {
  height: 100%;
}
.no-wrap {
  /* font-size: 12px; Adjust the size as necessary */
  white-space: nowrap;
}
</style>
