#Analyse Gpx
#Jarryd Dunn
#2018/02/12

from gpxTrack import gpxTrack
from gpxPoint import gpxPoint

def analyseLaps(laps):
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
        info["netEle"]=float(netEle)
        info['asc']=float(asc)
        info["desc"]=float(desc)
        info["aveHr"]=aveHr/len(lap)
        lapInfo.append(info)
    return lapInfo

def filterClimbs(laps):
    res=[]
    #First parse remove all climbs less than 100m
    for climb in laps:
        if climb["dist"]>=100 and climb["time"]>0:
            res.append(climb)
    #Second Parse group adjacent climbs and decents
    counter =0
    while counter< len(res)-1:
        if res[counter]["netEle"]!=0 and res[counter+1]["netEle"]!=0 and (res[counter]["netEle"]/abs(res[counter]["netEle"]))==(res[counter+1]["netEle"]/abs(res[counter+1]["netEle"])):
            pt = res[counter]
            pt2=res[counter+1]
            pt["dist"]+=pt2["dist"]
            pt["time"]+=pt2["time"]
            pt["netEle"]+=pt2["netEle"]
            pt["asc"]+=pt2["asc"]
            pt["desc"]+=pt2["desc"]
            pt["aveHr"]+=pt2["aveHr"]
            del res[counter+1]
        else:
            counter+=1
        
    return res

def printLapInfo(lapInfo):
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
    laps=track.split(500)
    lapInfo=analyseLaps(laps)
    printLapInfo(lapInfo)
    print()
    hills = track.splitClimbs()
    hillData = analyseLaps(hills)
    hillData = filterClimbs(hillData)
    printLapInfo(hillData)
    
    
                                                  
    
            
