import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RecommendView from "../views/RecommendView.vue";
import CompareSavingView from "../views/CompareSavingView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import MapView from "../views/MapView.vue";
import ArticleView from "../views/ArticleView.vue";
import ArticleDetailView from "../views/ArticleDetailView.vue";
import UserInfoView from "../views/User/UserInfoView.vue";
import MySaveView from "../views/User/MySaveView.vue";
import DepositView from "../views/SavingCompare/DepositView.vue";
import SavingView from "../views/SavingCompare/SavingView.vue";
import FreeSavingView from "../views/SavingCompare/FreeSavingView.vue";
import DepositDetailView from "../views/SavingCompare/DepositDetailView.vue";
import SavingDetailView from "../views/SavingCompare/SavingDetailView.vue";
import FreeSavingDetailView from "../views/SavingCompare/FreeSavingDetailView.vue";
import beforeLogin from "../views/User/beforeLogin.vue";
import { useUserStore } from "../stores/user";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/compareSaving",
      name: "compareSaving",
      component: CompareSavingView,
      children: [
        {
          path: "deposit",
          name: "deposit",
          component: DepositView,
        },
        {
          path: "saving",
          name: "saving",
          component: SavingView,
        },
        {
          path: "freeSaving",
          name: "freeSaving",
          component: FreeSavingView,
        },
        {
          path: "deposit/:fin_prdt_cd",
          name: "depositDetail",
          component: DepositDetailView,
        },
        {
          path: "saving/:fin_prdt_cd",
          name: "savingDetail",
          component: SavingDetailView,
        },
        {
          path: "freeSaving/:fin_prdt_cd",
          name: "freeSavingDetail",
          component: FreeSavingDetailView,
        },
        {
          path: "recommend",
          name: "recommend",
          component: RecommendView,
        },
      ],
    },
    {
      path: "/exchange",
      name: "exchange",
      component: ExchangeView,
    },
    {
      path: "/map",
      name: "map",
      component: MapView,
    },
    {
      path: "/articles",
      name: "article",
      component: ArticleView,
    },
    {
      path: "/articles/:id",
      name: "articleDetail",
      component: ArticleDetailView,
    },
    {
      path: "/mypage",
      name: "mypage",
      component: UserInfoView,
    },
    {
      path: "/mysave",
      name: "mysave",
      component: MySaveView,
    },
    {
      path: "/login",
      name: "logIn",
      component: beforeLogin,
    },
  ],
});

router.beforeEach((to, from) => {
  if (to.name === "compareSaving") {
    router.push({ name: "deposit" });
  }

  const userStore = useUserStore();
  if (to.name === "recommend") {
    if (!userStore.isLogin) {
      const check = confirm("로그인 후 조회 가능합니다.");
      if (check) {
        router.push({ name: "logIn" });
      } else {
        router.push(from);
      }
    }
  }
});

export default router;
