import openpyxl
import re
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy import distance
import geocoder
from geopy.distance import geodesic as GD
a=Nominatim(user_agent="Project")
data=pd.read_excel("New Microsoft Excel Worksheet.xlsx",sheet_name="Sheet1")
your_location=input("Enter your location:")
def distance(inital,final):
    a=Nominatim(user_agent="Project")
    place_1=a.geocode(inital)
    place_2=a.geocode(final)
    lat_1,long_1=(place_1.latitude),(place_2.longitude)
    lat_2,long_2=(place_2.latitude),(place_2.longitude)
    length_1=(lat_1,long_1)
    length_2=(lat_2,long_2)
    return(GD((lat_1,long_1),(lat_2,long_2)))
df=data.copy()
sortest=99999999999
shop_name=""
for i in (df[" city_state_zip"]):
    dist=distance(your_location,i)
    if dist<=sortest:
        shop_name=i
        sortest=dist
df=df[df[" city_state_zip"]==shop_name]                
print("Distance:",sortest)
print(df["Saree_Retailer_name"],(df["Mobile_1"]),(df[" contact_address"]))  