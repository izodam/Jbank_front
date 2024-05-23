// 금융 상품 저장 할 store
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useBankStore = defineStore(
  "bank",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const money = ref(0);

    const depositList = ref([]);
    const depositNormalList = ref([]);
    const depositDetail = ref([]);
    const isJoin = ref(false);
    const savingList = ref([]);
    const savingNormalList = ref([]);
    const savingDetail = ref([]);
    const freeSavingList = ref([]);
    const freeSavingNormalList = ref([]);
    const freeSavingDetail = ref([]);

    const bankList = ref([
      { fin_co_no: "", kor_co_nm: "전체보기" },
      { fin_co_no: "0010001", kor_co_nm: "우리은행" },
      { fin_co_no: "0010002", kor_co_nm: "한국스탠다드차타드은행" },
      { fin_co_no: "0010016", kor_co_nm: "대구은행" },
      { fin_co_no: "0010017", kor_co_nm: "부산은행" },
      { fin_co_no: "0010019", kor_co_nm: "광주은행" },
      { fin_co_no: "0010020", kor_co_nm: "제주은행" },
      { fin_co_no: "0010022", kor_co_nm: "전북은행" },
      { fin_co_no: "0010024", kor_co_nm: "경남은행" },
      { fin_co_no: "0010026", kor_co_nm: "중소기업은행" },
      { fin_co_no: "0010030", kor_co_nm: "한국산업은행" },
      { fin_co_no: "0010927", kor_co_nm: "국민은행" },
      { fin_co_no: "0011625", kor_co_nm: "신한은행" },
      { fin_co_no: "0013175", kor_co_nm: "농협은행주식회사" },
      { fin_co_no: "0013909", kor_co_nm: "하나은행" },
      { fin_co_no: "0014674", kor_co_nm: "주식회사 케이뱅크" },
      { fin_co_no: "0014807", kor_co_nm: "수협은행" },
      { fin_co_no: "0015130", kor_co_nm: "주식회사 카카오뱅크" },
      { fin_co_no: "0017801", kor_co_nm: "토스뱅크 주식회사" },
    ]);

    const findDetail = function (fin_prdt_cd, token) {
      axios({
        method: "get",
        url: `${API_URL}/savings/deposit-options/${fin_prdt_cd}/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          depositDetail.value = response.data.data;
          isJoin.value = response.data.isjoined;
          console.log(isJoin.value);
        })
        .catch((err) => console.log(err));
    };
    const findSavingDetail = function (fin_prdt_cd, token) {
      axios({
        method: "get",
        url: `${API_URL}/savings/saving-options/${fin_prdt_cd}/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          console.log(response.data);
          savingDetail.value = response.data.data;
          isJoin.value = response.data.isjoined;
          console.log(isJoin.value);
        })
        .catch((err) => console.log(err));
    };
    const findFreeSavingDetail = function (fin_prdt_cd, token) {
      axios({
        method: "get",
        url: `${API_URL}/savings/free-saving-options/${fin_prdt_cd}/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          freeSavingDetail.value = response.data.data;
          isJoin.value = response.data.isjoined;
          console.log(isJoin.value);
          // console.log(money.value);
          // console.log(depositDetail.value);
        })
        .catch((err) => console.log(err));
    };

    const recommendProduct = ref();

    const findRecommendProduct = function (token) {
      axios({
        method: "get",
        url: `${API_URL}/savings/recommend-products/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      }).then((res) => {
        recommendProduct.value = res.data;
      });
    };
    return {
      money,
      API_URL,
      depositList,
      depositNormalList,
      depositDetail,
      isJoin,
      savingList,
      savingNormalList,
      savingDetail,
      freeSavingList,
      freeSavingNormalList,
      freeSavingDetail,
      bankList,
      recommendProduct,
      findDetail,
      findSavingDetail,
      findFreeSavingDetail,
      findRecommendProduct,
    };
  },
  {
    persist: true,
  }
);
