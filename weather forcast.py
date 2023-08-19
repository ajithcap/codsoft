import requests
import json

# Get your API key from https://openweathermap.org/api
api_key = "19b1a697597d29f9f8ebe144d6d244e7"

# Enter a location name or coordinates
# Ask the user to enter a city name
location = input("Enter a city name in India: ")


# Make a request to the API with the location and the API key
base_url = "http://api.openweathermap.org/data/2.5/weather?"
params = {"q": location, "appid": api_key, "units": "metric"}
response = requests.get(base_url, params=params)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response as a JSON object
    data = response.json()

    # Extract the relevant information from the data
    temperature_celsius = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_type = data["weather"][0]["main"]

    # Print the weather forecast
    print(f"Weather Forecast for {location}:")
    print(f"Temperature: {temperature_celsius:.2f}°C")
    print(f"Humidity: {humidity:.2f}%")
    print(f"Wind Speed: {wind_speed:.2f} m/s")
    print(f"Weather Conditions: {weather_type}")

else:
    # Print an error message if the response is not successful
    print(f"Error: {response.status_code}")
