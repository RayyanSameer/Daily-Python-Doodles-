import requests
import sys 
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("OPENWEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def getweather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    } 

    try:
      
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200: 
            return response.json()
        elif response.status_code == 404:
            print(f"City '{city}' not found.")
        elif response.status_code == 401:
            print("Invalid API key. Check your .env file.")
        else:
            print(f"Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Network error. Check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return None

def display_weather(data):
    if not data:
        return
        
   
    city = data.get("name")  
    sys_data = data.get("sys", {})
    country = sys_data.get("country", "Unknown")
    
    main = data.get("main", {})
    temp = main.get("temp")
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")
    
    
    condition = data["weather"][0]["description"]
    wind = data.get("wind", {}).get("speed")

    print(f"\n {city}, {country}")
    print(f" {temp}°C (feels like {feels_like}°C)")
    print(f"  {condition.capitalize()}")
    print(f" Humidity: {humidity}%")
    print(f" Wind: {wind} m/s")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        city_name = input("Enter city name: ")
    else:
      
        city_name = " ".join(sys.argv[1:])
    
    if city_name:
        weather_data = getweather(city_name)
        display_weather(weather_data)