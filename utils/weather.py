import requests
import sys
from custom_exceptions.exceptions import TripPlannerExceptions

class WeatherForecastTool:
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, place:str):
        """
        getting the real current weather of a place
        """
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise TripPlannerExceptions(e, sys)
        
    def get_weather_forecast(self, place: str):
        """
        getting weather forecast of specific place
        """
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
                "cnt": 10,
                "unit": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise TripPlannerExceptions(e, sys)

        