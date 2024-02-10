<script setup lang="ts">
// import { Ref } from 'vue';
import { ref, onMounted, computed } from 'vue'
import { type out, get_weather } from '@/composables/weather';
import dayjs from 'dayjs'
const weather = ref<out | null>(null)


const geolocation_options = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0,
};


const updateWeather = async () => {
  console.log("Bazinga")
  navigator.geolocation.getCurrentPosition(async (e) => {
    const latitude = e.coords.latitude;
    const longitude = e.coords.longitude;
    weather.value = await get_weather(latitude, longitude)

  }, geolocation_error, geolocation_options);
}

const nextDaysTimestamps = computed(() => {
  return weather.value?.daily.time.slice(1)
})

function geolocation_error(e: any) {

}

const forecastHeaderDay = (date: any) => {
  const text = dayjs(date).format('DD, dddd')
  return text
}

onMounted(async () => {
  setTimeout(async () => {
    await updateWeather()
  }, 500)
  dayjs().format()
})


const current_iso = computed(() => {
  if (weather.value) {
    return weather.value.current.time.toISOString()
  } else return ''
})
</script>

<template>
  <header :class="{ 'has_timezone': (weather) }">
    <div id="headings">
      <h1 v-if="weather">{{ dayjs(current_iso).format('MMMM DD YYYY, dddd') }}</h1>
      <h1 v-else>Loading...</h1>
      <h2 v-if="weather">As of {{ dayjs(current_iso).format(`hh:mm A`) }}</h2>
    </div>
  </header>

  <main v-if="weather">
    <div id="current_weather">
      <h2>Current</h2>
      <p>
        Current Temperature: {{ weather.current.temperature2m.toPrecision(3) }}°C
      </p>
      <p>
        Felt Temperature: {{ weather.current.apparentTemperature.toPrecision(3) }}°C
      </p>

      <p>
        Wind Speed: {{ weather.current.windSpeed10m.toPrecision(3) }}
      </p>
      <p>
        Rain: {{ (weather.current.rain) ? weather.current.rain : 'No Rain.' }}
      </p>
    </div>
    
    <div id="current_forecast">
      
      <h2>Today's Forecasts</h2>
      <p>Highest Felt:{{ weather.daily.apparentTemperatureMax[0].toPrecision(3) }}°C</p>
      <p>Highest:{{ weather.daily.apparentTemperatureMin[0].toPrecision(3) }}°C</p>
      <p>Lowest: {{ weather.daily.temperature2mMax[0].toPrecision(3) }}°C</p>
      <p>Lowest Felt:{{ weather.daily.temperature2mMin[0].toPrecision(3) }}°C</p>
    </div>
  </main>

  <div id="forecast_weather" v-if="weather">
    <h1>Forecasts</h1>
    <ul>
      <li v-for="timestamp, i in nextDaysTimestamps" :key="i">
        <h2>{{ forecastHeaderDay(timestamp.toISOString()) }}</h2>
        <p>Highest Felt : {{ (weather.daily.apparentTemperatureMax[i]).toPrecision(3) }}°C</p>
        <p>Highest : {{ (weather.daily.temperature2mMax[i]).toPrecision(3) }}°C</p>
        <p>Lowest Felt : {{ (weather.daily.apparentTemperatureMin[i]).toPrecision(3) }}°C</p>
        <p>Lowest: {{ (weather.daily.temperature2mMin[i]).toPrecision(3) }}°C</p>
      </li>
    </ul>
  </div>
</template>

<style>
main {
  display: flex;
  flex-direction: row;
  max-width: 100vw;
  margin-bottom: 4vh;
}

main div {
  align-items: center;
  text-align: center;
  display: flex;
  flex-direction: column;
  width: 50vw;
}

#current_weather {
  text-align: center;
  margin-left: 15vw;
}

main h2 {
  margin: 1.5vh 0vw;
  font-size: clamp(1.4rem, 2vw, 3rem);

}

main p {
  margin: 1vh 0vw;
  font-size: clamp(1rem, 1.4vw, 2rem);

}

#current_forecast {
  margin-right: 15vw;
}


#forecast_weather {
  display: flex;
  margin-top: 5vh;
  bottom: 0;
  align-self: center;
  text-align: center;
  flex-direction: column;
}

#forecast_weather h1 {
  margin: 0.1vh 0vw;
  align-self: center;
}



ul {
  margin-top: 2.5%;
  align-self: center;
  align-items: center;
  width: 100%;
  display: flex;
  list-style: none;
}

li {
  width: 33.333%;
  font-size: clamp(0.5rem, 1.2vw, 3rem);
  padding-left: 2.5%;
  padding-right: 2.5%;
}

header {
  display: flex;
  justify-content: center;
  text-align: center;
  top: 0%;
  left: 0%;
  min-width: 100%;
  max-width: 100%;
}

header #headings {
  width: 80%;
  display: flex;
  flex-direction: column;
  padding: 1.2vh 1.2vw;
  margin: 2vh 2vw;
}

header #headings * {
  margin-top: 1vh;
  margin-bottom: 1vh;
  font-size: clamp(24px, 1.8vw, 48px);

}
</style>
