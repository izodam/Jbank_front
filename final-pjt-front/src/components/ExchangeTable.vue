<!-- 현재 환율 table -->
<template>
  <div class="m-5">
    <h3>현재 환율</h3>
    <small class="text-muted">오전 11시 이전에는 전날 환율이 나타납니다.</small>
    <table class="table table-hover">
      <caption>
        환율정보 -통화코드,국가/통화명,전신환(송금)받을때, 보낼때, 매매기준율,
        장부가격, 서울외국환중개, 매매기준율, 장부가격
      </caption>
      <thead>
        <tr>
          <th scope="col" rowspan="2">통화코드</th>
          <th scope="col" rowspan="2">국가/<br />통화명</th>
          <th scope="col" colspan="2">전신환(송금)</th>
          <th scope="col" rowspan="2">매매<br />기준율</th>
          <th scope="col" rowspan="2">장부<br />가격</th>
          <th scope="col" colspan="2">서울외국환중개</th>
        </tr>
        <tr>
          <th scope="col">받으실때</th>
          <th scope="col">보내실때</th>
          <th scope="col">매매기준율</th>
          <th scope="col">장부가격</th>
        </tr>
      </thead>
      <tbody id="dataList">
        <tr v-for="country in exchange.filter((c) => c.cur_unit !== 'KRW')">
          <td>
            <span>{{ country.cur_unit }}</span>
          </td>
          <td>{{ country.cur_nm }}</td>
          <td class="ar">{{ country.ttb }}</td>
          <td class="ar">{{ country.tts }}</td>
          <td class="ar">{{ country.deal_bas_r }}</td>
          <td class="ar">{{ country.bkpr }}</td>
          <td class="ar">{{ country.kftc_deal_bas_r }}</td>
          <td class="ar">{{ country.kftc_bkpr }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const props = defineProps({
  exchange: Array,
});

const exchange = props.exchange;

// console.log(store.exchange[0]);
</script>

<style scoped>
.table {
  width: 100%;
  border-top: 2px solid black;
  table-layout: fixed;
  line-height: 1.375;
  color: black;
  text-align: center;
}

.table thead th {
  background-color: #f1f2f4;
  border-bottom: 1px solid #dde1ea;
}
</style>
