<template>
  <div class="container mt-5 text-start">
    <div class="row justify-content-center">
      <div class="card shadow-lg border-0 px-0">
        <div class="card-header text-white text-center py-4">
          <h2 class="mb-0">Login</h2>
        </div>
        <div class="card-body p-4">
          <form @submit.prevent="logIn">
            <div class="form-group mb-3">
              <label for="username" class="form-label">Username</label>
              <input
                type="text"
                id="username"
                v-model.trim="username"
                class="form-control"
                required
              />
            </div>
            <div class="form-group mb-3">
              <label for="password" class="form-label">Password</label>
              <input
                type="password"
                id="password"
                v-model.trim="password"
                class="form-control"
                required
              />
            </div>
            <button type="submit" class="btn btn-primary w-100 py-2 mb-3">
              Login
            </button>
            <p v-if="store.notUser" class="not-user">
              아이디 및 비밀번호를 다시 확인해주세요
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";

const store = useUserStore();

const username = ref(null);
const password = ref(null);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin-top: 50px;
}

.card {
  border-radius: 15px;
  border: none;
}

.card-header {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  background-color: #1b3074;
  /* background-color: #2e4285; */
}

.card-body {
  padding: 30px;
}

.form-label {
  font-weight: 600;
  color: #333;
}

.form-control {
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 12px;
  font-size: 16px;
}

.form-control:focus {
  border-color: #144b81;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
}

.btn-primary {
  background-color: #102770;
  border: none;
  border-radius: 10px;
  padding: 10px;
  font-size: 18px;
  font-weight: 600;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.not-user {
  color: red;
  text-align: center;
}
</style>
