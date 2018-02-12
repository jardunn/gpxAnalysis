#gpxPoint
#Jarryd Dunn
#2018/02/12

class gpxPoint:
    def __init__(self,lat,long,time,elevation,hr):
        self.lat=lat
        self.long=long
        self.ele = elevation
        self.hr=hr
        self.time=time

    def __str__(self):
        return "latitude: {}, longitude: {}, time: {}, elevation: {}, heat rate: {}".format(self.lat,self.long,self.time,self.ele,self.hr)


if __name__=="__main__":
    p =gpxPoint(1,1,"12",10,154)
    print(p)
