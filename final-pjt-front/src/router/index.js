import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CompareSavingView from "../views/CompareSavingView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import MapView from "../views/MapView.vue";
import ArticleView from "../views/ArticleView.vue";
import UserInfoView from "../views/UserInfoView.vue";
import MySaveView from "../views/MySaveView.vue";
import DepositView from "../views/SavingCompare/DepositView.vue";
import SavingView from "../views/SavingCompare/SavingView.vue";
import FreeSavingView from "../views/SavingCompare/FreeSavingView.vue";
import DepositDetailView from "../views/SavingCompare/DepositDetailView.vue";

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
      path: "/article",
      name: "article",
      component: ArticleView,
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
  ],
});

router.beforeEach((to, from) => {
  if (to.name === "compareSaving") {
    router.push({ name: "deposit" });
  }
});

export default router;
