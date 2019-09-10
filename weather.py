import requests
import eel
API_ADDRESS = 'https://api.openweathermap.org/data/2.5/weather?appid=d0794456a9b267b1569ed57d73d121d9&q='

eel.init('web')

username = "empty"

@eel.expose
def getWeather(data):   
    url = API_ADDRESS+data
    jason_data = requests.get(url).json()
    formated_data = jason_data['weather'][0]['main']
    temp = jason_data['main']['temp']
    celsius_temp = temp-273.15
    wind_speed = jason_data['wind']['speed']
    print(formated_data)
    return formated_data

@eel.expose
def getUser(uname):
    username=uname
    print(username)
    
eel.start('index.html',size=(1000,600))