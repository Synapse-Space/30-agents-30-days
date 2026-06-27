import requests
from shared_core.config import config

class WeatherAPI:

    @staticmethod
    def get_coordinate(city:str):
        response=requests.get(
            config.WEATHER_GEOCODE_URL,
            params={
                "name":city,
                "count":1
            },
            timeout=20
        )

        response.raise_for_status()

        data=response.json()

        if "results" not in data:
            raise ValueError(
                f"City '{city}' not found."
            )

        result=data["results"][0]

        return {
            result["latitude"],
            result["longitude"]
        }

    @staticmethod
    def get_weather(city:str):

        latitue,longitude=(
            WeatherAPI.get_coordinate(city)
        )

        response=requests.get(
            config.WEATHER_API_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current":[
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m",
                    "weather_code"
                ]

            }
            timeout=20
        )

        response.raise_for_status()
        weather=response.json()["current"]

        return {
            "city":city,
            "temperature": weather["temperature_2m"],
            "humidity":weather["realtive_humidity_2m"],
            "wind_speed":weather["wind_speed_10m"],
            "weather_code":weather["weather_code"]
        }