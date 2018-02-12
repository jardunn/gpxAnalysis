#Analyse Gpx
#Jarryd Dunn
#2018/02/12

from gpxTrack import gpxTrack
from gpxPoint import gpxPoint

def analyseLap(laps):
    lapInfo = []
    for lap in laps:
        info={}
        dist=0
        time=0
        asc=0
        desc=0
        netEle=0
        aveHr=0
        for i in range(len(lap)):
            pt = lap[i]
            dist+=pt.dist
            if i>0:
                dEle=pt.ele-lap[i-1].ele
                netEle+=dEle
                if dEle>=0:
                    asc+= dEle
                else:
                    desc+=dEle
            aveHr+=pt.hr
        info["dist"]=dist
        info["time"]=lap[-1].duration-lap[0].duration
        info["netEle"]=netEle
        info['asc']=asc
        info["desc"]=desc
        info["aveHr"]=aveHr/len(lap)
        lapInfo.append(info)
    return lapInfo

def printLapInfo(laps):
    lapInfo = analyseLap(laps)
    counter =1
    headerStr="Lap\tDistance(m)\tTime(s)\tSpeed(kph)\tElevation(m)\tAscent\tDescent"
    hr = lapInfo[0]["aveHr"]!=-1
    if hr:
        headerStr+="\taveHR"

    print(headerStr)
    for lap in lapInfo:
        if hr:
            print("{:<1}\t{:<11.5}\t{:<7}\t{:<9.4}\t{:<9.5}\t{:<6.6}\t{:<6.6}\t{:<3}".format(counter,lap["dist"],lap["time"],(lap["dist"]/1000)/(lap["time"]/3600),lap["netEle"],lap["asc"],lap["desc"],lap["aveHr"]))
        else:
            print("{:<1}\t{:<11.5}\t{:<7}\t{:<9.4}\t{:<9.5}\t{:<6.6}\t{:<6.6}".format(counter,lap["dist"],lap["time"],(lap["dist"]/1000)/(lap["time"]/3600),lap["netEle"],lap["asc"],lap["desc"]))
        counter+=1

if __name__=="__main__":
    track = gpxTrack("test.gpx")
    laps=track.split(1000)
    printLapInfo(laps)
    
                                                  
    
            
