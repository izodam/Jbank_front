<template>
  <div class="container mt-5">
    <h3 v-if="userStore.myProduct.user.nickname">
      {{ userStore.myProduct.user.nickname }}님, 반갑습니다!
    </h3>
    <h3 v-else>Unknown 님!</h3>
    <div class="card custom-card mt-4">
      <div class="card-body">
        <div class="row me-2">
          <div class="col-11">
            <h5 class="mt-2">기본 정보</h5>
          </div>
          <div class="col-1">
            <button class="btn" @click="showModal">
              <span class="material-symbols-outlined">edit</span>
            </button>
          </div>
        </div>
        <hr />
        <p>이름 : {{ userStore.myProduct.user.nickname }}</p>
        <p>나이 : {{ userStore.myProduct.user.age }}</p>
        <p>Email : {{ userStore.myProduct.user.email }}</p>
        <p v-if="userStore.myProduct.user.money">
          자산 : {{ userStore.myProduct.user.money.toLocaleString("ko-KR") }}
        </p>
        <p v-else>자산 :</p>
        <p v-if="userStore.myProduct.user.salary">
          연봉 : {{ userStore.myProduct.user.salary.toLocaleString("ko-KR") }}
        </p>
        <p v-else>연봉 :</p>
      </div>
    </div>
    <div class="row">
      <div class="card mt-4 col-md-6 link-card" @click="goToRecommend">
        <div class="card-body p-4">
          <h5 class="title">나에게 가장 잘 맞는 상품은?</h5>
          <div class="copy1">
            <div>상품 추천 받으러 가기</div>
          </div>
        </div>
      </div>
      <div class="card mt-4 col-md-6 link-card" @click="goToMyProduct">
        <div class="card-body p-4">
          <h5 class="title">내 상품 금리 비교</h5>
          <div class="copy1">
            <div>내 가입 상품 보러가기</div>
          </div>
        </div>
      </div>
    </div>

    <!-- 모달 -->
    <div
      class="modal fade"
      id="editModal"
      tabindex="-1"
      aria-labelledby="editModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header" data-bs-theme="dark">
            <h5 class="modal-title" id="editModalLabel">회원정보 수정</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
              data-bs-theme="dark"
            ></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateProfile">
              <div class="mb-3">
                <label for="nickname" class="form-label">이름</label>
                <input
                  type="text"
                  class="form-control"
                  id="nickname"
                  v-model="form.nickname"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="age" class="form-label">나이</label>
                <input
                  type="number"
                  class="form-control"
                  id="age"
                  v-model="form.age"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="email" class="form-label">이메일</label>
                <input
                  type="email"
                  class="form-control"
                  id="email"
                  v-model="form.email"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="money" class="form-label">자산</label>
                <input
                  type="number"
                  class="form-control"
                  id="money"
                  v-model="form.money"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="salary" class="form-label">연봉</label>
                <input
                  type="number"
                  class="form-control"
                  id="salary"
                  v-model="form.salary"
                  required
                />
              </div>
              <button type="submit" class="btn btn-primary">수정하기</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import { onMounted } from "vue";
import axios from "axios";
import { useBankStore } from "@/stores/saving";
import { useRouter } from "vue-router";

let modal = null;

const router = useRouter();

const bankStore = useBankStore();
const userStore = useUserStore();

const form = ref({
  nickname: "",
  age: "",
  email: "",
  money: "",
  salary: "",
});

const showModal = () => {
  const modalElement = document.getElementById("editModal");
  modal = new bootstrap.Modal(modalElement);
  form.value = {
    nickname: userStore.myProduct.user.nickname,
    age: userStore.myProduct.user.age,
    email: userStore.myProduct.user.email,
    money: userStore.myProduct.user.money,
    salary: userStore.myProduct.user.salary,
  }; // 현재 회원정보를 폼에 채워줍니다.
  modal.show();
};

const updateProfile = () => {
  console.log("회원정보 수정:", form.value);
  // 여기서 실제로 회원정보를 서버에 업데이트하는 로직을 추가하세요.
  axios({
    method: "put",
    url: `${userStore.API_URL}/accounts/update/`,
    headers: { Authorization: `Token ${userStore.token}` },
    data: {
      nickname: nickname.value,
      age: age.value,
      email: email.value,
      money: money.value,
      salary: salary.value,
    },
  })
    .then((res) => {
      // console.log(res.data);
      userStore.findMyProduct();
      bankStore.findRecommendProduct(userStore.token);

      if (modal) {
        modal.hide();
      }
    })
    .catch((err) => console.log(err));
};

onMounted(() => {
  userStore.findMyProduct();
});

const goToRecommend = function () {
  router.push({ name: "recommend" });
};

const goToMyProduct = function () {
  router.push({ name: "mysave" });
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
.custom-card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.btn-primary {
  background-color: #2a3b5e;
  border: none;
}
.modal-header {
  background-color: #2a3b5e;
  color: white;
}

.row {
  /* display: flex; */
  flex-wrap: nowrap; /* Ensure the cards stay on one line */
  gap: 20px; /* Adjust the gap between the cards */
}

.link-card {
  border: 1px solid #ddd;
  transition: border-color 0.3s ease, box-shadow 0.3s ease; /* Add transition for border and box-shadow */
  flex: 1; /* Ensure the cards take up equal space */
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.link-card:hover {
  border-color: black;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Optional: Add shadow effect on hover */
}
</style>
