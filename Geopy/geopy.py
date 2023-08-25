from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def distance(city1, city2):
    geolocator = Nominatim(user_agent="specify")
    location = geolocator.geocode(city1)
    location2 = geolocator.geocode(city2)

    code1 = (location.latitude, location.longitude)
    code2 = (location2.latitude, location2.longitude)

    print(geodesic(code1, code2).miles)

distance("Accra","Ho")

