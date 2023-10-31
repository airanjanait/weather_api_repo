import requests
import json
 
def weather(city):
    print(city)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8bdaa78d3be525e032b4bf7d48ab83e0"
    
    print(url)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data=response.text
    print(type(data))
    
# converting data into json format______

    data_json=""
    data_json=json.loads(data)
    print(type(data_json))
    

    
# getting value from key______

    city=data_json["name"]
    wind_speed=data_json["wind"]["speed"]
    clouds=data_json["clouds"]["all"]
    humidity=data_json["main"]["humidity"]
    temperature=data_json["main"]["temp"]
    temp_celsius=round((temperature - 273.15),2)
    
    value=city,wind_speed,clouds,humidity,temp_celsius
    
    return value
    

