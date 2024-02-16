import { Injectable } from '@angular/core';
import { fetchWeatherApi } from 'openmeteo'
const url = "https://api.open-meteo.com/v1/forecast";


export const timezones = [
    "America/Anchorage",
    "America/Los_Angeles",
    "America/Denver",
    "America/Chicago",
    "America/New_York",
    "America/Sao_Paulo",
    "GMT",
    "Europe/London",
    "Europe/Berlin",
    "Europe/Moscow",
    "Africa/Cairo",
    "Asia/Bangkok",
    "Asia/Singapore",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Pacific/Auckland",
]

export type WeatherInfo = {
    current: {
        time: Date;
        temperature2m: number;
        apparentTemperature: number;
        rain: number;
        windSpeed10m: number;
    };
    daily: {
        time: Date[];
        temperature2mMax: Float32Array;
        temperature2mMin: Float32Array;
        apparentTemperatureMax: Float32Array;
        apparentTemperatureMin: Float32Array;
    }
};


@Injectable({
    providedIn: 'root'
  })
export class WeatherService {

  constructor() { }

  async get_weather(latitude: number, longitude: number): Promise<WeatherInfo> {
    const params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "rain", "wind_speed_10m"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min"],
        // "timezone": timezone,
        "forecast_days": 4
    };


    const responses = await fetchWeatherApi(url, params);

    const range = (start: number, stop: number, step: number) =>
        Array.from({ length: (stop - start) / step }, (_, i) => start + i * step);

    // Process first location. Add a for-loop for multiple locations or weather models
    const response = responses[0];

    // Attributes for timezone and location
    const utcOffsetSeconds = response.utcOffsetSeconds();

    const current = response.current()!;
    const daily = response.daily()!;

    // Note: The order of weather variables in the URL query and the indices below need to match!
    const weatherData: WeatherInfo = {
        current: {
            time: new Date((Number(current.time()) + utcOffsetSeconds) * 1000),
            temperature2m: current.variables(0)!.value(),
            apparentTemperature: current.variables(2)!.value(),
            rain: current.variables(3)!.value(),
            windSpeed10m: current.variables(4)!.value(),
        },
        daily: {
            time: range(Number(daily.time()), Number(daily.timeEnd()), daily.interval()).map(
                (t) => new Date((t + utcOffsetSeconds) * 1000)
            ),
            temperature2mMax: daily.variables(0)!.valuesArray()!,
            temperature2mMin: daily.variables(1)!.valuesArray()!,
            apparentTemperatureMax: daily.variables(2)!.valuesArray()!,
            apparentTemperatureMin: daily.variables(3)!.valuesArray()!,
        },

    };

    return weatherData
}
}
