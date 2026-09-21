# Weather App

A small Flask web app for checking current weather conditions by city name, built with Python and the OpenWeatherMap API.

## Features

- Search current weather by city name
- Looks up coordinates with the OpenWeatherMap Geocoding API, then fetches current conditions
- Shows temperature, humidity, wind speed, and recent precipitation
- Matches each condition to one of Google's weather icons
- Shows a friendly error message on the search page if a city isn't found or the API is unreachable
- Supports dark and light modes and stores the selected theme in localStorage

## Requirements

- Python 3+
- An OpenWeatherMap API key ([get one here](https://home.openweathermap.org/api_keys))
- Python packages listed in backend/requirements.txt

## Setup

1. From the `backend/` folder, install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file inside `backend/` with your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key
   ```

## Usage

From the `backend/` folder, run:
```
python app.py
```

Then open `http://localhost:5000` in your browser, enter a city name, and submit the form to see its current weather.

## Project structure

```
WeatherApp/
├── backend/
│   ├── app.py           # Flask routes
│   ├── weather.py       # OpenWeatherMap lookups + icon mapping
│   ├── requirements.txt
│   └── .env             # not committed — holds OPENWEATHER_API_KEY
├── templates/
│   ├── base.html
│   └── index.html       # search page  
└── static/
    ├── style.css
    └── img/search.svg
```

## Error handling

- If the city name isn't found, the search page shows an error message instead of crashing.
- If OpenWeatherMap is unreachable, the search page shows a generic "service unavailable" message.

## Known issues

- `backend/requirements.txt` is currently saved as UTF-16, which makes `pip install -r requirements.txt` fail on some systems. Regenerate it with `pip freeze > requirements.txt` from a working environment to save it as plain UTF-8.

## Stack

- Python
- Flask
- JavaScript
- HTML/CSS
- OpenWeatherMap API
- Geocoding API
- Current Weather API
