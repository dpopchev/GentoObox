# -*- coding: utf-8 -*-
###############################################################################
# conkyLatLong.py is a simple python script to obtain the longtitude/latitude
# for the machine it is run on based on the public ip address
#
#  Author: Kaivalagi
# Created: 09/10/2008

import socket, urllib2, re

def convertDegreeMinuteSecond(coord):
    coordparts = coord.split(".")

    degree = coordparts[0]

    minuteparts = str(float("."+coordparts[1]) * 60).split(".")

    minute = str(int(minuteparts[0]))

    second = str(float("."+minuteparts[1]) * 60)

    output = degree+"°"+minute+"\""+second+"'"

    return output

# setup default timeout of 10 seconds
socket.setdefaulttimeout(10)

# define the url to get geo data from
url = "http://gd.geobytes.com/gd?after=-1&variables=GeobytesLatitude,GeobytesLongitude"

# call the url, obtainined the lat/long data
usock = urllib2.urlopen(url)
latlongdata = usock.read()
usock.close()

# strip out lat/long from returned string
lat, long = re.match(r'.+sGeobytesLatitude="(-?\d+.\d+)";var sGeobytesLongitude="(-?\d+.\d+)".+',latlongdata).groups()

# convert to degree/minte/second

# output the lat/long with bearings...
if lat[0:1] == "-":
    lat = lat[1:len(lat)+1]
    lat = convertDegreeMinuteSecond(lat)+"S"
else:
    lat = convertDegreeMinuteSecond(lat)+"N"

if long[0:1] == "-":
    long = long[1:len(long)+1]
    long = convertDegreeMinuteSecond(long)+"W"
else:
    long = convertDegreeMinuteSecond(long)+"E"

print lat+" / "+long
