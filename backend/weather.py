import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_BASE = "https://www.gstatic.com/images/icons/material/apps/weather/2x"


class CityNotFoundError(Exception):
    """Raised when the geocoding API has no match for the given location."""


def get_coordinates(location):
    params = {"q": location, "limit": 1, "appid": API_KEY}
    geo_response = requests.get(GEOCODING_URL, params=params, timeout=10)
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if not geo_data:
        raise CityNotFoundError(f"Could not find a location matching '{location}'")

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]
    name = geo_data[0].get("name", location)

    return lat, lon, name


def get_weather(location, unit="metric"):
    lat, lon, name = get_coordinates(location)

    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": unit}
    weather_response = requests.get(WEATHER_URL, params=params, timeout=10)
    weather_response.raise_for_status()
    weather_data = weather_response.json()
    weather_data["_resolved_name"] = name

    return weather_data


def _icon_filename(weather_id, is_day):
    if 200 <= weather_id < 300:
        return "strong_tstorms_light_color_96dp.png"
    if 300 <= weather_id < 400:
        return "drizzle_light_color_96dp.png"
    if 500 <= weather_id < 505:
        return "showers_rain_light_color_96dp.png"
    if 500 <= weather_id < 600:
        return "heavy_rain_light_color_96dp.png"
    if 600 <= weather_id < 700:
        return "snow_showers_snow_light_color_96dp.png"
    if 700 <= weather_id < 800:
        return "haze_fog_dust_smoke_light_color_96dp.png"
    if weather_id == 800:
        return "sunny_light_color_96dp.png" if is_day else "clear_night_light_color_96dp.png"
    if weather_id == 801:
        return "mostly_sunny_light_color_96dp.png" if is_day else "mostly_clear_night_light_color_96dp.png"
    if weather_id == 802:
        return "partly_cloudy_light_color_96dp.png" if is_day else "partly_cloudy_night_light_color_96dp.png"
    if weather_id == 803:
        return "mostly_cloudy_day_light_color_96dp.png" if is_day else "mostly_cloudy_night_light_color_96dp.png"
    # 804 and anything unrecognized
    return "cloudy_light_color_96dp.png"


def get_icon_url(weather_data):
    """Map an OpenWeatherMap condition code to a Google weather icon URL."""
    weather_id = weather_data["weather"][0]["id"]
    sunrise = weather_data["sys"]["sunrise"]
    sunset = weather_data["sys"]["sunset"]
    is_day = sunrise <= weather_data["dt"] <= sunset

    return f"{ICON_BASE}/{_icon_filename(weather_id, is_day)}"