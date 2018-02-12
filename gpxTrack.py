#GPX object
#Jarryd Dunn
#2018/02/12

from gpxPoint import gpxPoint
import time
def splitTime(t):
    """takes a time string and converts to seconds since 1970/01/01"""
    yEnd = t.find("-")
    year = t[:yEnd]
    mEnd = t.find("-",yEnd+1)
    month = t[yEnd+1:mEnd]
    dEnd = t.find("T")
    day = t[mEnd+1:dEnd]
    hEnd=t.find(":")
    hour = t[dEnd+1:hEnd]
    minEnd = t.find(":",hEnd+1)
    minute = t[hEnd+1:minEnd]
    sec = t[minEnd+1:t.find("Z")]
    newT = time.strptime("{0} {1} {2} {3} {4} {5}".format(year,month,day,hour,minute,sec), "%Y %m %d %H %M %S")
    absTime = time.mktime(newT)
    return absTime

class gpxTrack:
    """Represents a gpx tracka as a set of points corrisponding to samples"""
    def __init__(self,fname):
        """Initialise gpxTrack from a gpx file"""
        self.points=[]
        self.dist=0
        f = open(fname,'r')
        text = f.readlines()
        lat=-1
        lon=-1
        ele=-1
        hr=-1
        time=-1
        for line in text:
            line=line.strip()
            if "lat" in line:
                latLoc = line.find("lat=")
                lat = line[latLoc+5:line.find('"',latLoc+6)]
                lonLoc =  line.find("lon=")
                lon = line[lonLoc+5:line.find('"',lonLoc+6)]
            if "ele" in line:
                ele = line[line.find("<ele>")+5:line.find("</ele>")]
            if "time" in line:
                time = line[line.find("<time>")+6:line.find("</time>")]
            if "/trkpt" in line:
                pt=gpxPoint(lat,lon,time,ele,hr)
                self.points.append(pt)
        self.points[0].dist=0
        baseT = splitTime(self.points[0].time) #starting time
        for i in range(1,len(self.points)):
            dist = self.points[i-1].getDist(self.points[i])
            self.points[i].dist=dist
            self.points[i].duration = int(splitTime(self.points[i].time)-baseT)
            self.dist+=dist
            
            

    def __str__(self):
        return "Length: "+str(self.dist)+"m"

    def split(self,dist):
        counter =0
        laps=[]
        lap=[]
        for pt in self.points:
            lap.append(pt)
            counter += pt.dist
            if counter >= dist:
                counter=0
                laps.append(lap)
                lap=[]
                
        laps.append(lap)
        return laps

if __name__ == "__main__":
    track = gpxTrack("test.gpx")
    print(track)
    pts = track.points
    laps = track.split(1000)
    print(splitTime(pts[0].time))
    print(len(laps))
