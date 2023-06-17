from obspy.clients.fdsn import Client
from obspy import UTCDateTime
client = Client("IRIS")

starttime = UTCDateTime("2018-01-01")
endtime = UTCDateTime("2019-01-01")
inventory = client.get_stations(network="IM", station="I*", starttime=starttime,
                                endtime=endtime, latitude= -7.540718, longitude= 110.445724, 
                                minradius=0, maxradius=30.0)
print(inventory)  
inventory.plot()