#GPX object
#Jarryd Dunn
#2018/02/12

from gpxPoint import gpxPoint

class gpxTrack:
    """Represents a gpx tracka as a set of points corrisponding to samples"""
    def __init__(self,fname):
        """Initialise gpxTrack from a gpx file"""
        self.points=[]
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

    def __str__(self):
        return "Length: "+str(len(self.points))
                
if __name__ == "__main__":
    track = gpxTrack("test.gpx")
    print(track)
    pts = track.points
    for i in range(10):
        print(pts[i])