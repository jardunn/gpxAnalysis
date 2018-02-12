#gpxPoint
#Jarryd Dunn
#2018/02/12

from math import sin,cos,atan,tan,sqrt,radians

class gpxPoint:
    def __init__(self,lat,long,time,elevation,dist=0,hr=-1):
        self.lat=float(lat)
        self.lon=float(long)
        self.ele = float(elevation)
        self.hr=int(hr)
        self.time=time
        self.dist=float(dist)

    def __str__(self):
        return "latitude: {}, longitude: {}, time: {}, elevation: {}, heat rate: {}".format(self.lat,self.lon,self.time,self.ele,self.hr)

    def getDist(self,other):
        """Approxomates the distance between this gpx point and another using Vincentry's formula"""
        a = 6378137.0 #semi-major axis
        f = 1/298.257223563 #flattening of elipsoid
        b = (1-f)*a #length of semi-major axis
        lat1 = self.lat
        lon1=self.lon
        lat2=other.lat
        lon2=other.lon
        u1 = atan((1-f)*tan(radians(lat1)))
        u2 = atan((1-f)*tan(radians(lat2)))
        L = radians(lon2-lon1)
        lam = L #Inital value from lambda
        
        sinU1=sin(u1)
        cosU1=cos(u1)
        sinU2=sin(u2)
        cosU2=cos(u2)
        
        dLam = 100
        while abs(dLam) > 1e-12:
            
            sinSigma = sqrt((cosU2*sin(lam))**2+(cosU1*sinU2-sinU1*cosU2*cos(lam))**2)
            cosSigma = sinU1*sinU2+cosU1*cosU2*cos(lam)
            sigma = atan(sinSigma/cosSigma)
            sinAlpha = (cosU1*cosU2*sin(lam))/sinSigma
            cos2alpha = 1-(sinAlpha)**2
            cos2SigmaM = cosSigma - ((2*sinU1*sinU2)/cos2alpha)
            C = (f/16)*cos2alpha*(4+f*(4-3*cos2alpha))
            lamNew = L+(1-C)*f*sinAlpha*(sigma+C*sinSigma*(cos2SigmaM+C*cosSigma*(-1+2*cos2SigmaM)))
            dLam = lam-lamNew
            lam=lamNew
        uSqr = cos2alpha*((a**2-b**2)/b**2)
        A =  1+(uSqr/16384)*(4096+uSqr*(-768+uSqr*(320-175*uSqr)))
        B = (uSqr/1024)*(256+uSqr*(-128+uSqr*(74-47*uSqr)))
        dSigma = B*sinSigma*(cos2SigmaM+0.25*B*(cosSigma*(-1+2*cos2SigmaM)-(B/6)*(cos2SigmaM*(-3+4*sinSigma**2)*(-3+4*cos2SigmaM))))
        s = b*A*(sigma-dSigma)
        alpha1 = atan((cosU2*sin(lam))/(cosU1*sinU2-sinU1*cosU2*cos(lam)))
        alpha2 = atan((cosU1*sin(lam))/(-1*sinU1*cosU2+cosU1*sinU2*cos(lam)))
        return s
        
            


if __name__=="__main__":
    p =gpxPoint(42.3541165,-71.0693514,"12",10,154)
    p2 = gpxPoint(40.7791472,-73.9680804,"12",10,154)
    print(p.getDist(p2))
