import geopy
import time


def textfixer():
    #locating the addresses through a landmark name
    #failure rate high b/c of bad data
    string = "location names,seperated by commas"
    array = string.split(",")
    geolocator = GoogleV3()
    file = open("locations.txt","w")
    for place in array:
        location = geolocator.geocode(place, timeout=20,components={"political":"New York", "locality":"Manhattan"})
        if location is None:
            file.write(place+"\n")
            file.write("None"+"\n")
            file.write("\n")
            time.sleep(2)
            continue
        file.write(place+"\n")
        file.write(location.address+"\n")
        file.write("\n")
    time.sleep(2)
    file.close()
    