<template>
  <div class="container mt-5 text-start">
    <div class="row justify-content-center">
      <div class="card shadow-lg border-0 px-0">
        <div class="card-header text-white text-center py-4">
          <h2 class="mb-0">Sign Up</h2>
        </div>
        <div class="card-body p-4">
          <form @submit.prevent="signUp">
            <div class="form-group mb-3">
              <label for="username" class="form-label">Username</label>
              <input
                type="text"
                id="username"
                v-model.trim="username"
                class="form-control"
                required
              />
              <p class="warning-message" v-if="store.wrong">
                중복된 id입니다. 다른 id를 사용하세요.
              </p>
            </div>
            <div class="form-group mb-3">
              <label for="password1" class="form-label">Password</label>
              <input
                type="password"
                id="password1"
                v-model.trim="password1"
                class="form-control"
                required
              />
              <p class="warning-message" v-if="!isValidPassword">
                비밀번호가 너무 짧습니다. 8~16자의 영문, 숫자, 특수문자를 사용해
                주세요.
              </p>
            </div>
            <div class="form-group mb-4">
              <label for="password2" class="form-label">Confirm Password</label>
              <input
                type="password"
                id="password2"
                v-model.trim="password2"
                class="form-control"
                required
              />
              <p class="warning-message" v-if="!isValidComfirmPassword">
                비밀번호가 일치하지 않습니다.
              </p>
            </div>
            <button type="submit" class="btn btn-primary w-100 py-2">
              Sign Up
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useUserStore } from "@/stores/user";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const store = useUserStore();

const isValidPassword = computed(() => {
  return (
    password1.value === null ||
    (password1.value.length >= 8 && password1.value.length <= 16)
  );
});

const isValidComfirmPassword = computed(() => {
  return password2.value === null || password1.value === password2.value;
});

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
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
  background-color: #102770;
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

.warning-message {
  color: rgb(216, 13, 13);
}

.notshow {
  display: none;
}
</style>
