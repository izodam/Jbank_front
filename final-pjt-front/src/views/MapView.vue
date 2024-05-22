<template>
  <div class="container-fluid mt-4">
    <div class="text-center my-4">
      <h3>주변 은행 검색</h3>
    </div>
    <div class="row">
      <!-- 검색창 -->
      <div
        :class="[
          'col-md-3',
          'search-form-wrapper',
          { expanded: isSearchFormOpen },
        ]"
      >
        <div
          class="search-form-container sticky-top p-4 bg-light rounded shadow-sm"
        >
          <button
            class="btn btn-secondary w-100 mb-3 toggle-btn"
            @click="toggleSearchForm"
          >
            {{ isSearchFormOpen ? "검색창 닫기" : "검색창 열기" }}
          </button>
          <transition name="slide-fade">
            <form v-if="isSearchFormOpen" @submit.prevent="searchPlaces">
              <div class="mb-3">
                <label for="province" class="form-label">도</label>
                <select
                  v-model="selectedProvince"
                  @change="updateCities"
                  class="form-select"
                  id="province"
                >
                  <option disabled value="">도 선택</option>
                  <option
                    v-for="(cities, province) in regions"
                    :key="province"
                    :value="province"
                  >
                    {{ province }}
                  </option>
                </select>
              </div>
              <div class="mb-3" v-if="selectedProvince">
                <label for="city" class="form-label">시</label>
                <select v-model="selectedCity" class="form-select" id="city">
                  <option disabled value="">시 선택</option>
                  <option
                    v-for="city in regions[selectedProvince]"
                    :key="city"
                    :value="city"
                  >
                    {{ city }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label for="bank" class="form-label">은행명</label>
                <select v-model="selectedBank" class="form-select" id="bank">
                  <option disabled value="">은행 선택</option>
                  <option
                    v-for="bank in store.bankList.slice(1)"
                    :key="bank.kor_co_nm"
                    :value="bank.kor_co_nm"
                  >
                    {{ bank.kor_co_nm }}
                  </option>
                </select>
              </div>
              <button type="submit" class="btn btn-secondary w-100 search-btn">
                검색
              </button>
            </form>
          </transition>
        </div>
      </div>
      <!-- 지도와 검색 결과 -->
      <div
        :class="['col-md-9', 'content-wrapper', { expanded: isSearchFormOpen }]"
      >
        <div class="row">
          <div class="col-md-8 col-xl-9">
            <KakaoMap
              :lat="37.566826"
              :lng="126.9786567"
              :level="5"
              @onLoadKakaoMap="onLoadKakaoMap"
              style="width: 100%; height: 500px"
            >
              <KakaoMapMarker
                v-for="(marker, index) in markerList"
                :key="index"
                :lat="marker.lat"
                :lng="marker.lng"
                :infoWindow="marker.infoWindow"
                :clickable="true"
                @onClickKakaoMapMarker="() => onClickMapMarker(marker)"
              />
            </KakaoMap>
          </div>
          <div class="col-md-4 col-xl-3">
            <div
              class="result-list p-3 bg-light rounded shadow-sm"
              style="height: 500px; overflow-y: auto"
            >
              <h5 class="mb-3">검색 결과</h5>
              <ul class="list-group">
                <li
                  v-for="(marker, index) in markerList"
                  :key="index"
                  class="list-group-item"
                  @click="highlightMarker(marker)"
                >
                  <strong>{{ marker.infoWindow.content }}</strong
                  ><br />
                  <small>{{ marker.address }}</small>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { KakaoMap, KakaoMapMarker } from "vue3-kakao-maps";
import { useBankStore } from "@/stores/saving";

const store = useBankStore();

const isSearchFormOpen = ref(false);
// 도와 시, 은행명을 포함한 데이터
const regions = {
  서울특별시: [
    "종로구",
    "중구",
    "용산구",
    "성동구",
    "광진구",
    "동대문구",
    "중랑구",
    "성북구",
    "강북구",
    "도봉구",
    "노원구",
    "은평구",
    "서대문구",
    "마포구",
    "양천구",
    "강서구",
    "구로구",
    "금천구",
    "영등포구",
    "동작구",
    "관악구",
    "서초구",
    "강남구",
    "송파구",
    "강동구",
  ],
  부산광역시: [
    "중구",
    "서구",
    "동구",
    "영도구",
    "부산진구",
    "동래구",
    "남구",
    "북구",
    "해운대구",
    "사하구",
    "금정구",
    "강서구",
    "연제구",
    "수영구",
    "사상구",
    "기장군",
  ],
  // 다른 도와 시들도 추가
  대구광역시: [
    "중구",
    "동구",
    "서구",
    "남구",
    "북구",
    "수성구",
    "달서구",
    "달성군",
  ],
  인천광역시: [
    "중구",
    "동구",
    "미추홀구",
    "연수구",
    "남동구",
    "부평구",
    "계양구",
    "서구",
    "강화군",
    "옹진군",
  ],
  광주광역시: ["동구", "서구", "남구", "북구", "광산구"],
  대전광역시: ["동구", "중구", "서구", "유성구", "대덕구"],
  울산광역시: ["중구", "남구", "동구", "북구", "울주군"],
  세종특별자치시: ["세종특별자치시"],
  경기도: [
    "수원시",
    "성남시",
    "의정부시",
    "안양시",
    "부천시",
    "광명시",
    "평택시",
    "동두천시",
    "안산시",
    "고양시",
    "과천시",
    "의왕시",
    "구리시",
    "남양주시",
    "오산시",
    "시흥시",
    "군포시",
    "의왕시",
    "하남시",
    "용인시",
    "파주시",
    "이천시",
    "안성시",
    "김포시",
    "화성시",
    "광주시",
    "양주시",
    "포천시",
    "여주시",
    "연천군",
    "가평군",
    "양평군",
  ],
  강원도: [
    "춘천시",
    "원주시",
    "강릉시",
    "동해시",
    "태백시",
    "속초시",
    "삼척시",
    "홍천군",
    "횡성군",
    "영월군",
    "평창군",
    "정선군",
    "철원군",
    "화천군",
    "양구군",
    "인제군",
    "고성군",
    "양양군",
  ],
  충청북도: [
    "청주시",
    "충주시",
    "제천시",
    "보은군",
    "옥천군",
    "영동군",
    "증평군",
    "진천군",
    "괴산군",
    "음성군",
    "단양군",
  ],
  충청남도: [
    "천안시",
    "공주시",
    "보령시",
    "아산시",
    "서산시",
    "논산시",
    "계룡시",
    "당진시",
    "금산군",
    "부여군",
    "서천군",
    "청양군",
    "홍성군",
    "예산군",
    "태안군",
  ],
  전라북도: [
    "전주시",
    "군산시",
    "익산시",
    "정읍시",
    "남원시",
    "김제시",
    "완주군",
    "진안군",
    "무주군",
    "장수군",
    "임실군",
    "순창군",
    "고창군",
    "부안군",
  ],
  전라남도: [
    "목포시",
    "여수시",
    "순천시",
    "나주시",
    "광양시",
    "담양군",
    "곡성군",
    "구례군",
    "고흥군",
    "보성군",
    "화순군",
    "장흥군",
    "강진군",
    "해남군",
    "영암군",
    "무안군",
    "함평군",
    "영광군",
    "장성군",
    "완도군",
    "진도군",
    "신안군",
  ],
  경상북도: [
    "포항시",
    "경주시",
    "김천시",
    "안동시",
    "구미시",
    "영주시",
    "영천시",
    "상주시",
    "문경시",
    "경산시",
    "군위군",
    "의성군",
    "청송군",
    "영양군",
    "영덕군",
    "청도군",
    "고령군",
    "성주군",
    "칠곡군",
    "예천군",
    "봉화군",
    "울진군",
    "울릉군",
  ],
  경상남도: [
    "창원시",
    "진주시",
    "통영시",
    "사천시",
    "김해시",
    "밀양시",
    "거제시",
    "양산시",
    "의령군",
    "함안군",
    "창녕군",
    "고성군",
    "남해군",
    "하동군",
    "산청군",
    "함양군",
    "거창군",
    "합천군",
  ],
  제주특별자치도: ["제주시", "서귀포시"],
};

const banks = ["국민은행", "신한은행", "우리은행", "하나은행", "농협은행"];

const map = ref(null);
const markerList = ref([]);
const selectedProvince = ref("");
const selectedCity = ref("");
const selectedBank = ref("");
const selectedMarker = ref(null);

const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
};

const searchPlaces = () => {
  if (!selectedProvince.value || !selectedCity.value || !selectedBank.value) {
    alert("모든 항목을 선택해 주세요.");
    return;
  }
  const query = `${selectedProvince.value} ${selectedCity.value} ${selectedBank.value}`;
  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(query, placesSearchCB);
};

const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();
    markerList.value = [];

    data.forEach((place) => {
      const marker = {
        lat: place.y,
        lng: place.x,
        infoWindow: {
          content: place.place_name,
          visible: false,
        },
        address: place.road_address_name || place.address_name,
      };
      markerList.value.push(marker);
      bounds.extend(new kakao.maps.LatLng(Number(place.y), Number(place.x)));
    });

    map.value?.setBounds(bounds);
  } else {
    alert("검색 결과가 없습니다.");
  }
};

const highlightMarker = (marker) => {
  // 기존 선택된 마커의 오버레이를 숨깁니다.
  if (selectedMarker.value) {
    selectedMarker.value.infoWindow.visible = false;
  }

  // 새로 선택된 마커의 오버레이를 표시합니다.
  marker.infoWindow.visible = true;
  selectedMarker.value = marker;

  // 선택된 마커 위치로 지도를 이동합니다.
  map.value.setCenter(new kakao.maps.LatLng(marker.lat, marker.lng));
};

const onClickMapMarker = (marker) => {
  highlightMarker(marker);
};

const updateCities = () => {
  selectedCity.value = "";
};

const toggleSearchForm = () => {
  isSearchFormOpen.value = !isSearchFormOpen.value;
};
</script>

<style>
.search-form-wrapper {
  transition: all 0.3s ease;
  overflow: hidden;
}

.search-form-wrapper {
  width: 120px; /* initial collapsed width */
}

.search-form-wrapper.expanded {
  width: 300px; /* expanded width */
}

.search-form-container {
  position: sticky;
  top: 20px;
  z-index: 1000;
  transition: all 0.3s ease;
}

.content-wrapper {
  transition: all 0.3s ease;
  width: calc(
    100% - 120px
  ); /* initial width adjusted for collapsed search form */
}

.content-wrapper.expanded {
  width: calc(100% - 300px); /* width adjusted for expanded search form */
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  max-height: 0;
  opacity: 0;
}

.result-list {
  height: 500px;
  overflow-y: auto;
}

.list-group-item {
  cursor: pointer;
}

.list-group-item:hover {
  background-color: #f0f0f0;
}

.toggle-btn {
  background-color: #777;
}

.toggle-btn:hover {
  background-color: #464555;
  border-color: #464555;
  /* color: black; */
}

.search-btn {
  background-color: #51606e;
  border-color: #51606e;
}

.search-btn:hover {
  background-color: #6a7987;
  border-color: #6a7987;
  /* color: black; */
}
</style>
