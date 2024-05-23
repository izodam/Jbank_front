<template>
  <div class="container mt-3">
    <div v-if="userStore.myProduct.user.nickname && store.recommendProduct">
      <div class="row align-items-center">
        <div class="col-md-10">
          <p class="mb-1">
            {{ userInfo.age }}세, 연봉
            {{ userInfo.salary.toLocaleString("ko-KR") }}원, 자산
            {{ userInfo.money.toLocaleString("ko-KR") }}원인
          </p>
          <h2>
            <strong class="name">{{ userInfo.nickname }}</strong
            >님의 추천 상품
          </h2>
        </div>
        <div class="col-md-2">
          <button class="btn btn-dark" @click="showModal">
            AI에게 추천받기
          </button>
          <div
            class="modal fade my-0"
            id="editModal"
            tabindex="-1"
            aria-labelledby="editModalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <ChatComponent />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="best mt-4">
          <h5>비슷한 사람들은, 이러한 상품을 많이 가입했어요!</h5>
          <div class="row mt-3">
            <div
              v-for="item in store.recommendProduct.data1"
              class="col-12 col-md-4 mb-4"
            >
              <div class="card item-card w-100">
                <div class="card-body">
                  <h5 class="card-title">{{ item.fin_prdt_nm }}</h5>
                  <h6 class="card-subtitle mb-2 text-body-secondary">
                    {{ item.kor_co_nm }}
                  </h6>
                  <p class="card-text">최고 우대 금리 : {{ item.max_rate }}%</p>
                  <button
                    class="btn btn-secondary join-btn"
                    @click="changeJoin(item.fin_prdt_cd, item.prdt_type)"
                    v-if="!item.is_joined"
                  >
                    가입하기
                  </button>
                  <button
                    class="btn btn-secondary cancle-btn"
                    @click="changeCancle(item.fin_prdt_cd, item.prdt_type)"
                    v-else
                  >
                    가입취소
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="max-rate mt-4">
          <h5>회원님에게 추천하는 금리가 높은 상품들이에요!</h5>
          <div class="row mt-3">
            <div
              v-for="item in store.recommendProduct.data2"
              class="col-12 col-md-4 mb-4"
            >
              <div class="card item-card w-100">
                <div class="card-body">
                  <h5 class="card-title">{{ item.fin_prdt_nm }}</h5>
                  <h6 class="card-subtitle mb-2 text-body-secondary">
                    {{ item.kor_co_nm }}
                  </h6>
                  <p class="card-text">최고 우대 금리 : {{ item.max_rate }}%</p>
                  <button
                    class="btn btn-secondary join-btn"
                    @click="changeJoin(item.fin_prdt_cd, item.prdt_type)"
                    v-if="!item.is_joined"
                  >
                    가입하기
                  </button>
                  <button
                    class="btn btn-secondary cancle-btn"
                    @click="changeCancle(item.fin_prdt_cd, item.prdt_type)"
                    v-else
                  >
                    가입취소
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="userStore.myProduct.user.nickname">
      <p class="mb-1">
        {{ userInfo.age }}세, 연봉
        {{ userInfo.salary.toLocaleString("ko-KR") }}원, 자산
        {{ userInfo.money.toLocaleString("ko-KR") }}원인
      </p>
      <h2>
        <strong class="name">{{ userInfo.nickname }}</strong
        >님의 추천 상품
      </h2>
      <div v-if="store.recommendProduct === null" class="mt-4">
        <h5>회원님과 비슷한 유저가 없네요...</h5>
        <p>AI에게 추천 받으실래요?</p>
        <div>
          <button class="btn btn-dark" @click="showModal">
            AI에게 추천받기
          </button>
          <div
            class="modal fade my-0"
            id="editModal"
            tabindex="-1"
            aria-labelledby="editModalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <ChatComponent />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="mt-5 no-info p-3">
      <h2 class="mb-4">기본 정보를 입력해야 <br />추천이 가능합니다.</h2>
      <button class="btn btn-secondary" @click="goToUserInfo">
        입력하러 가기
      </button>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { useBankStore } from "@/stores/saving";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import ChatComponent from "@/components/ChatComponent.vue";

const userStore = useUserStore();
const store = useBankStore();
const router = useRouter();

const userInfo = userStore.myProduct.user;
let modal = null;

const showModal = () => {
  const modalElement = document.getElementById("editModal");
  modal = new bootstrap.Modal(modalElement);

  modal.show();
};

const goToUserInfo = function () {
  router.push({ name: "mypage" });
};

const changeJoin = function (fin_prdt_cd, prdt_type) {
  const check = confirm("가입하시겠습니까?");
  if (check) {
    axios({
      method: "post",
      url: `${store.API_URL}/accounts/join-product/`,
      headers: { Authorization: `Token ${userStore.token}` },
      data: {
        prdt_type: prdt_type,
        fin_prdt_cd: fin_prdt_cd,
      },
    })
      .then((res) => {
        store.findRecommendProduct(userStore.token);
      })
      .catch((err) => console.log(err));
  }
};

const changeCancle = function (fin_prdt_cd, prdt_type) {
  const check = confirm("정말 취소하시겠습니까?");
  if (check) {
    axios({
      method: "post",
      url: `${store.API_URL}/accounts/cancel-product/`,
      data: {
        prdt_type: prdt_type,
        fin_prdt_cd: fin_prdt_cd,
      },
      headers: { Authorization: `Token ${userStore.token}` },
    })
      .then((res) => {
        store.findRecommendProduct(userStore.token);
      })
      .catch((err) => console.log(err));
  }
};
onMounted(() => {
  if (userStore.myProduct.user.nickname) {
    store.findRecommendProduct(userStore.token);
  }
});

console.log(store.recommendProduct);
</script>

<style scoped>
.name {
  color: #52608b;
}

.no-info {
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.item-card {
  margin-right: 1rem;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  height: 100%;
}

.join-btn:hover {
  background-color: #1b3074;
  color: white;
  /* height: 60px; */
}

.join-btn {
  background-color: #e6e6e3;
  color: black;
  border-color: #e6e6e3;
}

.cancle-btn:hover {
  background-color: #e6e6e3;
  color: black;
  border-color: #e6e6e3;
}

.modal-body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
