import os
import sys
import json
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


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
    get_weather(location, unit)

if __name__ == "__main__":
    main()


    
    