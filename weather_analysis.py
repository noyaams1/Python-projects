import requests
import json
import os

FILE_NAME = "weather_data.json"


# ---------- Load / Save ----------
def save_to_file(data, filename=FILE_NAME):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_from_file(filename=FILE_NAME):
    if os.path.exists(filename):
        with open(filename) as f:
            return json.load(f)
    return None


# ---------- Fetch Weather ----------
def fetch_weather_data():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=32.8184&longitude=34.9885"
        "&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        "&start_date=2025-05-04&end_date=2025-05-04"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data:", response.status_code)
        return None


# ---------- Statistical Analysis ----------
def analyze_weather(data):
    temps = data["hourly"]["temperature_2m"]
    humidity = data["hourly"]["relative_humidity_2m"]
    wind_speed = data["hourly"]["wind_speed_10m"]

    return {
        "avg_temp": sum(temps) / len(temps),
        "max_temp": max(temps),
        "min_temp": min(temps),
        "avg_humidity": sum(humidity) / len(humidity),
        "avg_wind_speed": sum(wind_speed) / len(wind_speed),
    }


# ---------- Display ----------
def display_weather_results(data, analysis):
    print("\n📍 Location: Kiryat Bialik, IL")

    current = data.get("current", {})
    print("\n🌤 Current weather:\n")
    print(f"Temperature: {current.get('temperature_2m')} °C")
    print(f"Humidity: {current.get('relative_humidity_2m')} %")
    print(f"Wind Speed: {current.get('wind_speed_10m')} km/h")

    print("\n📊 Statistical Analysis:\n")
    print(f"Average temperature: {analysis['avg_temp']:.2f} °C")
    print(f"Maximum temperature: {analysis['max_temp']} °C")
    print(f"Minimum temperature: {analysis['min_temp']} °C")
    print(f"Average humidity: {analysis['avg_humidity']:.2f} %")
    print(f"Average wind speed: {analysis['avg_wind_speed']:.2f} km/h")


# ---------- Main ----------
def main():
    data = load_from_file()
    if not data:
        data = fetch_weather_data()
        if data:
            save_to_file(data)
        else:
            print("❌ Failed to retrieve weather data.")
            return

    analysis = analyze_weather(data)
    display_weather_results(data, analysis)


# ---------- Run ----------
if __name__ == "__main__":
    main()
