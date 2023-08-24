from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

def weatherfunction(city):
    owm = OWM('1ed6c31eb154acfec2d026b566ed7fb7')
    mgr = owm.weather_manager()

    reg = owm.city_id_registry()
    list_of_tuples = reg.ids_for(city, matching='exact')
    code=list_of_tuples[0][2]
    cityy=list_of_tuples[0][1]


    if len(list_of_tuples) > 1:

# Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place(cityy)
        w = observation.weather

        print(w.detailed_status)        # 'clouds'
        print(w.wind())                  # {'speed': 4.6, 'deg': 330}
        print(w.humidity)               # 87
        print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        print(w.rain)             # {}
        w.heat_index              # None
        w.clouds          
    else:
        print("Your city doesnot seem to be correct")

intake = input("Please enter your City ")
weatherfunction(intake)
