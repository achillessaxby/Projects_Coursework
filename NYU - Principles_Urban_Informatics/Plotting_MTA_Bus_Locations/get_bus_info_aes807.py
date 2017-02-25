from __future__ import print_function
import sys
import csv
import pylab as pl
import json
import urllib as ulr
import os

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

totalData = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(sys.argv[3], 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
    
    i = 0
    
    for total in totalData:
        longitude = totalData[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        latitude = totalData[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    
        if (totalData[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}):
            Stop_Name = 'N/A'
            Stop_Status = 'N/A'

        else:
            Stop_Name = totalData[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            Stop_Status = totalData[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

        writer.writerow([latitude,longitude,Stop_Name,Stop_Status])
        i += 1
