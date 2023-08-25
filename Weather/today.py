from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('1ed6c31eb154acfec2d026b566ed7fb7')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Accra,GH')
w = observation.weather

print(w.detailed_status)        # 'clouds'
print(w.wind())                  # {'speed': 4.6, 'deg': 330}
print(w.humidity)               # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)             # {}          # {}
w.heat_index              # None
w.clouds                  # 75