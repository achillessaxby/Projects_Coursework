from __future__ import print_function
import sys
import pylab as pl
import json
import urllib as ulr
import os

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2] 

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

totalData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

i = 0

print ("Bus Line: %s" %(sys.argv[2]))
print ("The Number of Actve Buses: %d" %(len(totalData)))

for total in totalData:
    longitude = totalData[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = totalData[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print ("Bus %d is at the latitude %f and at the longitude %f" %(i,latitude,longitude))
    i += 1

