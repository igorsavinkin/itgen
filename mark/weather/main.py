city_name = input("Введите название города: ")
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
language = get_default_config()
language['language'] = 'ru'
owm = OWM('635a0dfd52beedcddc2f621ce12f890d', language)
manager = get_default_config()
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city_name)
print(observation.weather)
weather = observation.weather
print('сейчас на улице:',weather.detailed_status)
print('облачность:',weather.clouds,'%')
print('текущая температура:',weather.temperature("celsius").get("temp"),'градуса(ов)')
print('максимальная температура:',weather.temperature("celsius").get("temp_max"),'градуса(ов)')
print('сейчас ощущается:', weather.temperature("celsius").get("feels_like"), 'градуса(ов)')
print('минимальная температура',weather.temperature("celsius").get("temp_min"),'градуса(ов)')
print('за последний час выпало осадков:',weather.rain,'мм')
print('скорость ветра:',weather.wind(),'м/с')
print(weather.temperature)