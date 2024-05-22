import { createApp } from "vue";
import { createPinia } from "pinia";
import { useKakao } from "vue3-kakao-maps/@utils";

// console.log(import.meta.env.VITE_appkey);
import App from "./App.vue";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);
useKakao(import.meta.env.VITE_appkey);

app.use(pinia);
app.use(router);

app.mount("#app");
