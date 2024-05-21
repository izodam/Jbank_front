<template>
  <div class="d-md-grid gap-2 col-md-8 mx-auto">
    <h2 class="text-center mb-4">환율 계산</h2>
    <div class="row div-card">
      <!-- 왼쪽 카드 -->
      <div class="col-md-6 mb-5">
        <div class="card">
          <select
            class="card-header form-select"
            aria-label="Default select example"
            v-model="beforeCountry"
          >
            <option v-for="country in exchange">
              {{ country.cur_nm.split(" ")[0] }}
            </option>
          </select>
          <div class="card-body">
            <div class="form-group">
              <label for="amount">금액</label>
              <input
                type="number"
                class="form-control"
                id="amount"
                v-model="beforeAmount"
                placeholder="금액을 입력하세요"
              />
              <!-- <p>{{ beforeCurrency }}</p> -->
            </div>
          </div>
        </div>
      </div>
      <!-- 오른쪽 카드 -->
      <div class="col-md-6 mb-5">
        <div class="card">
          <select
            class="card-header form-select"
            aria-label="Default select example"
            v-model="afterCountry"
          >
            <option v-for="country in exchange">
              {{ country.cur_nm.split(" ")[0] }}
            </option>
          </select>

          <div class="card-body card-right text-end">
            <p class="mt-3" v-show="afterAmout !== 0">
              {{ afterAmout }}
              <strong>{{ currency }}</strong>
            </p>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 text-center">
          <button class="btn btn-primary m-2" @click="calculateExchange">
            환전 계산
          </button>
          <button class="btn btn-primary" @click="clear">초기화</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  exchange: Array,
});

const exchange = props.exchange;
import { ref } from "vue";

const beforeCountry = ref("한국");
const beforeAmount = ref(null);

const afterCountry = ref("미국");
const afterAmout = ref(0);

const currency = ref("");
const beforeCurrency = ref("");

const calculateExchange = function () {
  if (beforeAmount.value <= 0) {
    window.alert("값을 다시 확인하세요!!");
  } else {
    const before = ref(null);
    const after = ref(null);
    exchange.forEach((element) => {
      if (element.cur_nm.split(" ")[0] === beforeCountry.value) {
        before.value = parseFloat(element.tts.replace(/,/g, ""));
        if (element.cur_unit.includes("100")) {
          before.value /= 100;
        }
        beforeCurrency.value = element.cur_nm.split(" ")[1];
        if (!beforeCurrency.value) {
          beforeCurrency.value = element.cur_nm.split(" ")[0];
        }
      }
      if (element.cur_nm.split(" ")[0] === afterCountry.value) {
        after.value = parseFloat(element.ttb.replace(/,/g, ""));
        if (element.cur_unit.includes("100")) {
          after.value /= 100;
        }
        currency.value = element.cur_nm.split(" ")[1];
        console.log(currency.value);
        if (!currency.value) {
          currency.value = element.cur_nm.split(" ")[0];
        }
      }
    });
    if (before.value === 0) {
      afterAmout.value =
        Math.round((beforeAmount.value / after.value) * 100) / 100;
    } else if (after.value === 0) {
      console.log(before.value);
      afterAmout.value =
        Math.round(beforeAmount.value * before.value * 100) / 100;
    } else {
      const rate = before.value / after.value;
      afterAmout.value = Math.round(rate * beforeAmount.value * 100) / 100;
    }
  }
};

const clear = function () {
  beforeAmount.value = 0;
  afterAmout.value = 0;
};
</script>

<style scoped>
.card-right {
  height: 94px;
}
</style>
