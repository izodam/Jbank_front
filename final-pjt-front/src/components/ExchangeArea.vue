<template>
  <div class="exchange-calculator">
    <h2 class="text-center mb-4">환율 계산</h2>
    <div class="row mb-3">
      <!-- 왼쪽 카드 -->
      <div class="col-md-6 mb-3 mb-md-0 d-flex justify-content-end">
        <div class="card h-100">
          <div
            class="card-header d-flex justify-content-between align-items-center"
          >
            <custom-dropdown
              :exchange="exchange"
              :selected-country="beforeCountry"
              @update:selectedCountry="beforeCountry = $event"
            />
            <button
              class="btn btn-outline-secondary ms-2"
              @click="swapCountries"
            >
              <i class="fas fa-exchange-alt"></i>
            </button>
          </div>
          <div class="card-body">
            <div class="form-group">
              <!-- <label for="amount" class="form-label">금액</label> -->
              <div class="input-group input-group-lg">
                <input
                  type="number"
                  class="form-control"
                  id="amount"
                  v-model="beforeAmount"
                  placeholder="금액을 입력하세요"
                  aria-describedby="inputGroup-sizing-lg"
                />
                <span
                  class="input-group-text"
                  aria-describedby="inputGroup-sizing-lg"
                  >{{ beforeCurrency }}</span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 오른쪽 카드 -->
      <div class="col-md-6 d-flex justify-content-start">
        <div class="card h-100">
          <div class="card-header">
            <custom-dropdown
              :exchange="exchange"
              :selected-country="afterCountry"
              @update:selectedCountry="afterCountry = $event"
            />
          </div>
          <div class="card-body text-end">
            <p class="exchange-result" v-show="afterAmount !== 0">
              {{ afterAmount }}
              <strong>{{ currency }}</strong>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12 text-center">
        <button class="btn btn-primary m-2" @click="calculateExchange">
          <i class="fas fa-calculator"></i> 계산
        </button>
        <button class="btn btn-secondary" @click="clear">
          <i class="fas fa-undo"></i> 초기화
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import CustomDropdown from "./CustomDropdown.vue";

const props = defineProps({
  exchange: Array,
});

const exchange = props.exchange;
import { ref } from "vue";

const beforeCountry = ref("미국");
const beforeAmount = ref(null);
const afterCountry = ref("한국");
const afterAmount = ref(0);
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
        if (!currency.value) {
          currency.value = element.cur_nm.split(" ")[0];
        }
      }
    });
    if (before.value === 0) {
      afterAmount.value =
        Math.round((beforeAmount.value / after.value) * 100) / 100;
    } else if (after.value === 0) {
      afterAmount.value =
        Math.round(beforeAmount.value * before.value * 100) / 100;
    } else {
      const rate = before.value / after.value;
      afterAmount.value = Math.round(rate * beforeAmount.value * 100) / 100;
    }
  }
};

const clear = function () {
  beforeAmount.value = 0;
  afterAmount.value = 0;
};

const swapCountries = function () {
  const temp = beforeCountry.value;
  beforeCountry.value = afterCountry.value;
  afterCountry.value = temp;
};
</script>

<style scoped>
.exchange-calculator {
  margin: 0 auto;
}

.card {
  /* max-width: 600px; */
  width: 600px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-label {
  font-weight: bold;
}

.input-group-text {
  background-color: #ffffff;
  border-color: #ffffff;
}

.exchange-result {
  margin-top: 1rem;
  font-size: 1.25rem;
}

.btn {
  cursor: pointer;
}

.btn-primary {
  background-color: #1b3074;
}
.btn-primary:hover {
  background-color: #44507a;
}

.btn {
  width: 100px;
}
.btn-secondary:hover {
  background-color: #6c757d;
}
.form-group {
  margin-top: 1rem;
}

.btn-outline-secondary:hover {
  background-color: white;
  color: black;
}

.btn-outline-secondary {
  width: 10%;
  border-color: #f8f9fa;
}
</style>
