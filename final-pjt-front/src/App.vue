<template>
  <nav class="navbar navbar-expand-lg navbar-custom" data-bs-theme="dark">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <RouterLink :to="{ name: 'home' }" class="navbar-brand ms-2">
        Jbank
      </RouterLink>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <RouterLink :to="{ name: 'compareSaving' }" class="nav-link">
              예금 비교
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'exchange' }" class="nav-link">
              환율 계산기
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'map' }" class="nav-link">
              주변 은행
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'article' }" class="nav-link">
              커뮤니티
            </RouterLink>
          </li>
          <li v-if="userStore.isLogin" class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              id="navbarDropdown"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              data-bs-display="static"
            >
              <!-- <span class="material-symbols-outlined"> account_circle </span> -->
              {{ userStore.nowUserName }}님
            </a>
            <ul class="dropdown-menu dropdown-menu-end profile-dropdown">
              <li>
                <RouterLink :to="{ name: 'mypage' }" class="dropdown-item">
                  내 프로필
                </RouterLink>
              </li>
              <li>
                <RouterLink :to="{ name: 'mysave' }" class="dropdown-item">
                  내 가입상품
                </RouterLink>
              </li>
              <div class="dropdown-divider"></div>
              <li><a class="dropdown-item" @click="logout">로그아웃</a></li>
            </ul>
          </li>
          <li v-else class="nav-item">
            <RouterLink :to="{ name: 'logIn' }" class="nav-link">
              로그인
            </RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <RouterView class="use-font" />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useUserStore } from "./stores/user";

const userStore = useUserStore();

const logout = function () {
  userStore.logOut();
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&family=Orbit&display=swap");

.navbar-nav {
  font-family: "Noto Sans KR", sans-serif;
  font-weight: 500;
}

.use-font {
  font-family: "Noto Sans KR", sans-serif;
}
.navbar-custom {
  background-color: #1b3074; /* 네이비 블루 */
  padding: 0.75rem 1rem;
}
.navbar-custom .navbar-brand {
  color: #ffffff;
  font-weight: bold;
}
.navbar-custom .nav-link {
  color: #ffffff;
  margin-right: 1rem;
  position: relative;
  transition: color 0.3s ease;
}
.navbar-custom .nav-link:hover {
  color: #daeceb; /* 스카이 블루 */
}
.navbar-custom .nav-link::after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: #daeceb; /* 스카이 블루 */
  transition: width 0.3s;
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
}
.navbar-custom .nav-link:hover::after,
.navbar-custom .router-link-active::after {
  width: 100%;
}
.navbar-custom .dropdown-menu {
  background-color: #1b3074;
}
.navbar-custom .dropdown-item {
  color: #ffffff;
  transition: background-color 0.3s ease;
}
.navbar-custom .dropdown-item:hover {
  background-color: #002244;
}
.navbar-custom .navbar-toggler-icon {
  color: #ffffff;
}
.profile-dropdown {
  width: 100%;
  text-align: end;
}

@media (max-width: 992px) {
  .profile-dropdown {
    text-align: left; /* 작은 화면에서는 왼쪽 정렬 */
  }
}

.material-symbols-outlined {
  font-variation-settings: "FILL" 0, "wght" 400, "GRAD" 0, "opsz" 48;
}
</style>
