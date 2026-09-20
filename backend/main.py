import os
import sys
import json
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_coordinates(location):
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={1}&appid={API_KEY}"
    geo_response = requests.get(geocoding_url)
    geo_data = geo_response.json()

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    return lat, lon


def get_weather(location, unit):
    lat, lon = get_coordinates(location)

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={unit}"

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    print(weather_data["main"]["temp"])

def get_forecast(location, unit):
    lat, lon = get_coordinates(location)

    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units={unit}"

    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    for forecast in forecast_data["list"]:
        temperature = forecast["main"]["temp"] - 273.15
        print(f"{forecast['dt_txt']} - {temperature:.1f}°C")


def main():
    if len(sys.argv) != 3:
            sys.exit("Input the location and unit")
    location = sys.argv[1].upper()
    unit = sys.argv[2].upper()

    if unit == "C":
        unit = "metric"
        symbol = "°C"
    elif unit == "F":
        unit = "imperial"
        symbol = "°F"
    else:
        sys.exit("Unit must be C or F")
    get_weather(location, unit)

if __name__ == "__main__":
    main()


    
    