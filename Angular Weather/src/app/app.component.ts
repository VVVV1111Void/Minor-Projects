import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { WeatherService, WeatherInfo } from './weather.service';
import { Dayjs } from 'dayjs';
const GeolocationOptions = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0,
};

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  providers: [WeatherService]
})
export class AppComponent implements OnInit {
  title = 'weather';
  // dayjs = new Dayjs()
  ngOnInit() {
    // this.dayjs.format()
    this.updateWeather()
    console.log("Banana")
  }


  async updateWeather() {
    navigator.geolocation.getCurrentPosition(async (e) => {
        const latitude = e.coords.latitude;
        const longitude = e.coords.longitude;
        // weather.value = await WeatherService(latitude, longitude)

    }, this.geolocationError, GeolocationOptions);
}

  // async getForecasts

  convert_to_iso(weather: WeatherInfo) {
      return weather.current.time.toISOString()
  }

  async geolocationError() {
    // temp error
    console.log("failed to get location.")
  }
}


// const nextDaysTimestamps = computed(() => {
//   return weather.value?.daily.time.slice(1)
// })

// const forecastHeaderDay = (date: any) => {
//   const text = dayjs(date).format('DD, dddd')
//   return text
// }


