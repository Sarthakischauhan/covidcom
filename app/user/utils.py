from math import dist
import geopy
import geopy.distance
from geopy.geocoders import Nominatim
import haversine as hs
import time
from oauth2client import client 
import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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


def scrapeCowin(state=None,district=None):
    url = "https://dashboard.cowin.gov.in/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    innerBox=soup.find_all("div",{"class_":["inner", "innerbox"]})
    print(innerBox)


def authorizeGspread():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
    client = gspread.authorize(creds)
    return client

def getvaclink():
    client = authorizeGspread()
    sheet = client.open("Links_for_Vaccine").sheet1
    return sheet.col_values(1)[1:]

def addresourcelink(type_,link):
    client = authorizeGspread()
    sheet = client.open("Waitlist").sheet1
    insertRow = [link,type_]
    sheet.append_row(insertRow)
