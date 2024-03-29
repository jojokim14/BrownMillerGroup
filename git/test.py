import csv
import subprocess
from geopy.geocoders import GoogleV3
from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely.geometry.polygon import LinearRing
import time


def contains(point, polygon):
    boolean = polygon.contains(point)
    return boolean

def test():
    point = Point(0.5,0.5)
    r2 = LinearRing([
                (1.1),
                (0, 0),
                (1, 0),
                (0, 1)])
    polygon2 = Polygon(r2)
    boolean = polygon2.contains(point)
    print (boolean)

def main():
    geolocator = GoogleV3()
    file = open("./approved/fie-name.csv", "w+")
    error = open("./error/file-name.csv", "w+")
    rejects = open("./rejects/file-name.csv","w+")
    writer = csv.writer(file)
    ewriter = csv.writer(error)
    rwriter = csv.writer(rejects)
    with open('AVERY4.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
        	#district coordinates
            r1 = LinearRing(([
                (1.1),
                (0, 0),
                (1, 0),
                (0, 1)]))
            polygon1 = Polygon(r1)
            r2 = LinearRing([
                (1.1),
                (0, 0),
                (1, 0),
                (0, 1)])
            polygon2 = Polygon(r2)
                #96 to 59
            string = row[2]+" "+row[3]+" "+row[4]
            location = geolocator.geocode(string, timeout=20)
            if location is None:
                ewriter.writerow(row)
                time.sleep(2)
                continue
            x = location.latitude
            y = location.longitude
            split1 = location.address.split(", ")
            split2 = split1[2].split(" ")
            if len(split2) > 1:
                zip = split2[1]
                row[5] = zip
            print(string)
            point = Point(x, y)
            bool1 = contains(point, polygon1)
            #print (bool1)
            bool2 = contains(point, polygon2)
            #print (bool2)
            if bool1 or bool2:
                writer.writerow(row)
            else:
                rwriter.writerow(row)
            time.sleep(1)
    file.close()
    f.close()
    error.close()

if __name__ == "__main__":
    main()


