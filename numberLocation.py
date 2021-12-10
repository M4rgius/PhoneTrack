import phonenumbers
import folium
from phonenumbers import geocoder

from myNumber import number

Key = '0ba6b90e6f1a4a5ab4001d61dcfaf47f'
ch_number = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(ch_number, "en")
print(yourLocation)

#service Provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

#save map in html file

myMap.save("myLocation.html")