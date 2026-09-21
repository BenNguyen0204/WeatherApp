import requests
from flask import Flask, request, render_template

from weather import get_weather, get_icon_url, CityNotFoundError

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        location = request.form.get("location", "").strip()
        if not location:
            return render_template("index.html", error="Enter a city name.")

        try:
            data = get_weather(location)
        except CityNotFoundError:
            return render_template("index.html", error=f"Couldn't find \"{location}\".")
        except requests.RequestException:
            return render_template("index.html", error="Weather service is unavailable right now.")

        rain_last_hour = data.get("rain", {}).get("1h", 0)
        weather_info = {
            "city": data.get("_resolved_name") or data.get("name") or location,
            "temp": round(data["main"]["temp"]),
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "precipitation": round(rain_last_hour, 1),
            "description": data["weather"][0]["description"],
            "icon_url": get_icon_url(data),
        }

        return render_template("index.html", weather=weather_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)