import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "your personal api key goes here"

def displayWeather(data,city):
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']

       print("***********************")
       print(f"City: {city}")
       print(f"Temperature: {temperature}° C")
       print(f"Humidity: {humidity} %")
       print(f"Pressure: {pressure} hPa")
       print(f"Weather Report: {report[0]['description']}")

def getWeather(city):
    units = "metric"
    URL = BASE_URL + "units=" + units + "&q=" + city + "&appid=" + API_KEY
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       displayWeather(data,city)
    else:
       # showing the error message
       print("Error in the HTTP request")


#getWeather("Winnipeg")
#getWeather("Chicago")
#getWeather("Islamabad")
