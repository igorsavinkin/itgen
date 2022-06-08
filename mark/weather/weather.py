from pyowm import OWM
from pyowm.utils.config import get_default_config
language = get_default_config()
language = ['language'] = 'ru'
own = OWN('635a0dfd52beedcddc2f621ce12f890d',language)
manager = get_default_config()
observation = manager.weather_at_place('')