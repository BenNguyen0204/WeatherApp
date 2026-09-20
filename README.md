# Weather App

A lightweight command-line tool to check current weather conditions from your terminal, built with Python and the OpenWeather API.

## Features

- Search weather by location
- Supports Celsius and Fahrenheit
- Uses the OpenWeather Geocoding API to get coordinates
- Gets the current temperature

## Requirements

- Python 3.8+
- An OpenWeather API key ([get one here](https://home.openweathermap.org/api_keys))

## Setup

1. Install the required packages:
   ```
   pip install requests python-dotenv
   ```

2. Create a `.env` file in the project root and add your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key
   ```

## Usage

For Celsius:
```
python main.py "City name" C
```

For Fahrenheit:
```
python main.py "City name" F
```

### Example output

```
```

## Error Handling

- If the city name isn't found, the app will print an error message instead of crashing.
- If the API key is missing or invalid, the app will notify you to check your `.env` file.

## Stack

- Python