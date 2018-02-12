#Analyse GPX
#Jarryd Dunn
#2018/02/12

from gpxTrack import gpxTrack
from gpxPoint import gpxPoint

if __name__ == "__main__":
    fname = "test.gpx"
    track = gpxTrack(fname)
    print(track)

