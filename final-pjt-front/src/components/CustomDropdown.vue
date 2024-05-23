<template>
  <div class="dropdown w-100">
    <button
      class="btn btn-light dropdown-toggle w-100"
      type="button"
      id="dropdownMenuButton"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      {{ selectedCountry }}
    </button>
    <div class="dropdown-menu w-100 p-2" aria-labelledby="dropdownMenuButton">
      <div class="d-flex flex-wrap">
        <div
          v-for="country in exchange"
          :key="country.cur_nm"
          class="country-card p-2"
          @click="selectCountry(country)"
        >
          <p>{{ country.cur_nm.split(" ")[0] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    exchange: Array,
    selectedCountry: String,
  },
  methods: {
    selectCountry(country) {
      this.$emit("update:selectedCountry", country.cur_nm.split(" ")[0]);
    },
  },
};
</script>

<style scoped>
.country-card {
  /* border: 1px solid #f7f7f7; */
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  /* background-color: #f8f9fa; */
  transition: background-color 0.2s;
  width: 25%;
}

.country-card:hover {
  color: #1b3074;
  font-weight: bolder;
}
</style>
