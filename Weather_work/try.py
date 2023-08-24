from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=1ed6c31eb154acfec2d026b566ed7fb7')
pprint(r.json)