    # Built-in API request by city name from OpenWeather

import requests
from secrets import OpenWeather
from datetime import datetime, timezone, timedelta
import logging

# print(OpenWeather["API_KEY"])
API_KEY = OpenWeather["API_KEY"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def kelvin_to_celsius(c):
    c -= 273.15
    c = round(c, 1)
    return c

def kelvin_to_fahrenheit(f):
    f = (f - 273.15) * 9 / 5 + 32
    f = round(f, 1)
    return f

def ms_to_kmh(m):
    m *= 3.6
    m = round(m, 2)
    return m

def to_local_time(ts, offset_ts):
    local_time = datetime.fromtimestamp(ts, tz=timezone.utc) + timedelta(seconds=offset_ts)
    at_time = local_time.strftime("%H:%M:%S")
    return at_time

def wind_direction(degrees):
    compass_directions = [
        "North", "North-Northeast", "Northeast", "East-Northeast",
        "East", "East-Southeast", "Southeast", "South-Southeast",
        "South", "South-Southwest", "Southwest", "West-Southwest",
        "West", "West-Northwest", "Northwest", "North-Northwest"
    ]
    # Each compass direction spans 22.5°
    index = round(degrees / 22.5) % 16
    return compass_directions[index]

def get_current_weather_report():

    while True:
        logger = logging.getLogger()

        city = input("For which city would you like a weather report? (type 'no' to exit the program)\n")

        if city == "no":
            print("Exiting current weather report...")
            break

        url = f"{BASE_URL}q={city}&appid={API_KEY}"

        try:
            data = requests.get(url, verify=False).json()
            # print(data)

            country = data["sys"]["country"]
            current_weather = data["weather"][0]["description"]
            cloud =  data["clouds"]["all"]
            tempt = data["main"]["temp"]
            temp_feel = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            sea_level = data["main"]["sea_level"]
            ground_level = data["main"]["grnd_level"]
            visibility = data["visibility"]
            wind_speed = data["wind"]["speed"]
            wind_dir = data["wind"]["deg"]
            sunrise_ts = data["sys"]["sunrise"]
            sunset_ts = data["sys"]["sunset"]
            timezone_offset = data["timezone"]

            if data["cod"] == 200:
                print(
                    f"""
                            Weather Report for {city.capitalize().strip()}, {country}:
                            🌍 Current Weather: {current_weather.capitalize()} with {cloud}% cloud coverage
                            🌡️ Temperature: {kelvin_to_celsius(tempt)}°C ({kelvin_to_fahrenheit(tempt)}°F) and feels like {kelvin_to_celsius(temp_feel)}°C ({kelvin_to_fahrenheit(temp_feel)}°F)
                                • Min Temperature: {kelvin_to_celsius(temp_min)}°C ({kelvin_to_fahrenheit(temp_min)}°F)
                                • Max Temperature: {kelvin_to_celsius(temp_max)}°C ({kelvin_to_fahrenheit(temp_max)}°F)
                            💦 Humidity: {humidity}%
                            ⛵ Pressure:
                                • Sea level: {sea_level} hPa
                                • Ground level: {ground_level} hPa
                            👁️ Visibility: {round(visibility/1000)}km
                            💨 Wind: 
                                • Speed: {wind_speed} m/s ({ms_to_kmh(wind_speed)} km/h)
                                • Direction: {wind_dir}° (blowing from the {wind_direction(wind_dir)})
                            🌄 Sunrise: {to_local_time(sunrise_ts, timezone_offset)}
                            🌇 Sunset: {to_local_time(sunset_ts, timezone_offset)}
                            """
                )

        except Exception as e:
            logger.warning("Users may make typos.")
            print("Invalid request. Please try again.")

get_current_weather_report()

