// 금융 상품 저장 할 store
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useBankStore = defineStore("bank", () => {
  const API_URL = "http://127.0.0.1:8000";

  const depositList = ref([
    {
      id: 1,
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001B",
      kor_co_nm: "우리은행",
      fin_prdt_nm: "WON플러스예금",
      join_way: "인터넷,스마트폰,전화(텔레뱅킹)",
      mtrt_int:
        "만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기예금 금리",
      spcl_cnd: "해당사항 없음",
      join_deny: 1,
      join_member: "실명의 개인",
      etc_note:
        "- 가입기간: 1~36개월\n- 최소가입금액: 1만원 이상\n- 만기일을 일,월 단위로 자유롭게 선택 가능\n- 만기해지 시 신규일 당시 영업점과 인터넷 홈페이지에 고시된 계약기간별 금리 적용",
      max_limit: null,
      dcls_strt_day: "20240424",
      dcls_end_day: null,
      fin_co_subm_day: "202404240919",
      "6month_before": 2.0,
      "6month_after": 3.0,
      "12month_before": 2.2,
      "12month_after": 3.2,
      "24month_before": 2.4,
      "24month_after": 3.4,
      "36month_before": 2.6,
      "36month_after": 3.6,
    },
    {
      id: 2,
      dcls_month: "202404",
      fin_co_no: "0010002",
      fin_prdt_cd: "00320342",
      kor_co_nm: "한국스탠다드차타드은행",
      fin_prdt_nm: "e-그린세이브예금",
      join_way: "인터넷,스마트폰",
      mtrt_int:
        "만기 후 1개월: 약정이율의 50%\n만기 후 1개월 초과 1년 이내: 약정이율의 30%\n만기 후 1년 초과: 약정이율의 10%",
      spcl_cnd:
        "1.SC제일은행 최초 거래 신규고객에 대하여 우대 이율을 제공함 (보너스이율0.2%)                     2.SC제일마이백통장에서 출금하여 이 예금을 신규하는경우에 보너스이율을 제공함\n(가입기간:1년제/ 보너스이율:0.1% / 만기해약하는 경우에 한해 보너스이율을 적용함)",
      join_deny: 1,
      join_member: "개인(개인사업자 포함)",
      etc_note: "디지털채널 전용상품 (인터넷, 모바일뱅킹)",
      max_limit: 1000000000,
      dcls_strt_day: "20240502",
      dcls_end_day: "99991231",
      fin_co_subm_day: "202405021135",
      "6month_before": 2.0,
      "6month_after": 3.0,
      "12month_before": 2.2,
      "12month_after": 3.2,
      "24month_before": 2.4,
      "24month_after": 3.4,
      "36month_before": 2.6,
      "36month_after": 3.6,
    },
  ]);
  const savingList = ref([
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      kor_co_nm: "우리은행",
      fin_prdt_nm: "우리SUPER주거래적금",
      join_way: "영업점,인터넷,스마트폰,전화(텔레뱅킹)",
      mtrt_int:
        "만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리",
      spcl_cnd:
        "1. 아래 각 항(가, 나)의 조건을 충족하는 경우 합산 최대 연 1.9%p 우대\n가. 우리은행을 처음 거래하시는 고객 : 연 1.0%p\n나. 거래실적 인정기간 동안 아래 거래실적을 계약기간별 필수기간(1년 : 6개월, 2년 : 12개월, 3년 : 18개월)이상 충족하는 경우 최대 연 0.9%p",
      join_deny: "1",
      join_member: "실명의 개인",
      etc_note:
        "1. 가입기간 : 1년, 2년, 3년\n(가입기간별 금리 차등적용)\n2. 가입금액 : 월 50만원 이내",
      max_limit: null,
      dcls_strt_day: "20240422",
      dcls_end_day: null,
      fin_co_subm_day: "202404221107",
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001L",
      kor_co_nm: "우리은행",
      fin_prdt_nm: "WON적금",
      join_way: "스마트폰,전화(텔레뱅킹)",
      mtrt_int:
        "만기 후\n- 1개월이내 : 만기시점약정이율×50%\n- 1개월초과 6개월이내: 만기시점약정이율×30%\n- 6개월초과 : 만기시점약정이율×20%\n\n※ 만기시점 약정이율 : 일반정기적금 금리",
      spcl_cnd:
        "1. 아래 각 항(가, 나)의 조건을 충족하는 경우 합산 최대 연 0.2%p 우대\n가. 이 적금을 우리꿈통장, WON통장에 연결하여 가입하는 경우 : 0.1%p\n나. 우리 오픈뱅킹 서비스에 타행계좌가 등록되어 있는 경우 : 연 0.1%p",
      join_deny: "1",
      join_member: "실명의 개인",
      etc_note: "1. 가입기간 : 1년\n2. 가입금액 : 월 50만원 이내",
      max_limit: null,
      dcls_strt_day: "20240422",
      dcls_end_day: null,
      fin_co_subm_day: "202404221107",
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010002",
      fin_prdt_cd: "00266451",
      kor_co_nm: "한국스탠다드차타드은행",
      fin_prdt_nm: "퍼스트가계적금",
      join_way: "영업점,인터넷,스마트폰",
      mtrt_int:
        "만기 후 1개월: 약정이율의 50%\n만기 후 1개월 초과 1년 이내: 약정이율의 30%\n만기 후 1년 초과: 약정이율의 10%",
      spcl_cnd: "없음",
      join_deny: "1",
      join_member: "개인(개인사업자 포함)",
      etc_note: "해당없음",
      max_limit: 10000000,
      dcls_strt_day: "20240422",
      dcls_end_day: "99991231",
      fin_co_subm_day: "202404221005",
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010016",
      fin_prdt_cd: "10521001000846001",
      kor_co_nm: "대구은행",
      fin_prdt_nm: "내손안에 적금",
      join_way: "스마트폰",
      mtrt_int:
        "만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%",
      spcl_cnd:
        "* 최고우대금리 : 연0.55%p\n -대구은행 인터넷뱅킹,스마트뱅킹을 통하여 최초로 적립식예금 가입 시 : 연0.20%p\n - 상품 가입 전 최근 3개월 이내 대구은행 인터넷,스마트 뱅킹을 통한 이체거래 3회 이상 : 연0.10%p\n- 상품 가입 전 수수료우대 통장 보유 고객 : 연0.20%p\n* 상품을 스마트뱅킹을 통해 가입 시 : 연0.05%p",
      join_deny: "1",
      join_member: "실명의 개인",
      etc_note:
        "1.1계좌당 가입한도 : 월 100만원(최저 10만원 이상)\n2.iM뱅크 전용상품",
      max_limit: 1000000,
      dcls_strt_day: "20240422",
      dcls_end_day: null,
      fin_co_subm_day: "202404220958",
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010016",
      fin_prdt_cd: "10527001000925000",
      kor_co_nm: "대구은행",
      fin_prdt_nm: "영플러스적금",
      join_way: "영업점,인터넷,스마트폰",
      mtrt_int:
        "만기 후 1개월 미만 경과: 약정이자율 x 50%\n만기 후 3개월 미만 경과: 약정이자율 x 25%\n만기 후 3개월 이상 경과: 약정이자율 x 10%",
      spcl_cnd:
        "* 최고우대금리 : 연0.55%p\n- 상품 가입 전 영플러스통장 보유 또는 재예치일 기준 영플러스통장 전월 평잔 10만원 이상 : 연0.10%p\n- 예금기간 중 입금횟수 10회 이상 : 연0.10%p\n- 입학 및 졸업 축하금리 : 연0.30%p\n*상품을 인터넷/스마트뱅크를 통해 가입시 우대 : 연0.05%p",
      join_deny: "3",
      join_member: "만 29세 이하 개인",
      etc_note: "1계좌당 가입한도 : 월 50만원(최저 1만원 이상)",
      max_limit: 500000,
      dcls_strt_day: "20240422",
      dcls_end_day: null,
      fin_co_subm_day: "202404220958",
    },
  ]);
  const savingOption = ref([
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "S",
      rsrv_type_nm: "정액적립식",
      save_trm: "12",
      intr_rate: 2.75,
      intr_rate2: 4.65,
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "S",
      rsrv_type_nm: "정액적립식",
      save_trm: "24",
      intr_rate: 2.8,
      intr_rate2: 4.7,
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "S",
      rsrv_type_nm: "정액적립식",
      save_trm: "36",
      intr_rate: 2.85,
      intr_rate2: 4.75,
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "F",
      rsrv_type_nm: "자유적립식",
      save_trm: "12",
      intr_rate: 2.55,
      intr_rate2: 4.45,
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "F",
      rsrv_type_nm: "자유적립식",
      save_trm: "24",
      intr_rate: 2.6,
      intr_rate2: 4.5,
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001F",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "F",
      rsrv_type_nm: "자유적립식",
      save_trm: "36",
      intr_rate: 2.65,
      intr_rate2: 4.55,
    },
    {
      dcls_month: "202404",
      fin_co_no: "0010001",
      fin_prdt_cd: "WR0001L",
      intr_rate_type: "S",
      intr_rate_type_nm: "단리",
      rsrv_type: "S",
      rsrv_type_nm: "정액적립식",
      save_trm: "12",
      intr_rate: 4,
      intr_rate2: 4.2,
    },
  ]);

  const bankList = ref([
    "우리은행",
    "한국스탠다드차타드은행",
    "대구은행",
    "부산은행",
    "광주은행",
    "제주은행",
    "전북은행",
  ]);

  const fillDepositList = function () {
    if (depositList.length === 0) {
      axios({
        method: "get",
        url: `${API_URL}/deposit-products/`,
      })
        .then((response) => {
          depositList.value = response.data;
        })
        .catch((err) => console.log(err));
    }
  };

  return {
    API_URL,
    depositList,
    savingList,
    savingOption,
    bankList,
    fillDepositList,
  };
});
