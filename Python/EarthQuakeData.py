import json
from urllib.request import urlopen

# Setup.
# First, you must get the URL, then open *urllib.request.urlopen()* and read the resulting
# HTTPRequest object *HTTPRequestObject.read()*. After, load *JSON.loads()* the data into python form.

print("Loading JSON and loading info...")
urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"
webURL = urlopen(urlData).read()
jData = json.loads(webURL)
print("Data for: '" + jData['metadata']['title'] + "' has finished loading...")

def printSmall(eqInfo):
    #Print all "small" earthquakes from the resulting JSON information.
    print("Displaying all 'small' earthquakes (0-3.99 magnitude).")
    for i in eqInfo['features']:
        mag = i["properties"]["mag"]
        if mag < 4.0:
            print(i["properties"]["place"], " | Mag: " + str(mag))

def printMedium(eqInfo):
    #Print all "medium" earthquakes from resulting JSON information.
    print("Displaying all 'medium' earthquakes (4.0-6.99 magnitude).")
    for i in eqInfo['features']:
        mag = i["properties"]["mag"]
        if mag >= 4 and mag < 7:
            print(i["properties"]["place"], " | Mag: " + str(mag))

def printLarge(eqInfo):
    #Print all "big" earthquakes from resulting JSON information.
    print("Displaying all 'big' earthquakes (7-10 magnitude).")
    for i in eqInfo['features']:
        mag = i['properties']['mag']
        if mag >= 7:
            print(i["properties"]["place"], " | Mag: " + str(mag))

def main():
    #Run all of the different functions. Only pass in the data we recieved from translating the JSON into
    #python dictionary by using jData = json.loads(webURL) *Line 11*.
    printSmall(jData)
    print("-----------------------------------")
    printMedium(jData)
    print("-----------------------------------")
    printLarge(jData)


if __name__ == '__main__':
    main()
