from math import dist
import geocoder
import geopy
import geopy.distance
from geopy.geocoders import Nominatim
import haversine as hs
import time 
import sel


def getLocation():
    s = geocoder.ip("me")
    return s.latlng

def rangingUsers(loc1,loc2):
    point = geopy.Point(loc1,loc2)
    d = geopy.distance.distance(kilometers=2)
    final = d.destination(point=point, bearing=0)
    return final,point

def calculate(loc1,loc2):
    distance = hs.haversine(loc1,loc2)
    print(distance)


nom = Nominatim(user_agent="Covidcom")

def loctoAddress(latitude,longitude,language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return nom.reverse(coordinates, language=language).raw
    except:
        return loctoAddress(latitude, longitude)


def scrapeCowin(state,district):
    url = "https://dashboard.cowin.gov.in/"