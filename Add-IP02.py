# Python Program to classify an IP address
#
# Potential subroutines to use
#
# 2.  python-geoip
#
#     https://pythonhosted.org/python-geoip/
#
#     >> pip install python-geoip
#
#     If you also want the free MaxMind Geolite2 database you can in addition:
#
#     >> pip install python-geoip-geolite2
#
# 
#     If you have installed the python-geoip-geolite2 package you can start using the GeoIP database right away:
#
#
from geoip import geolite2
import ipaddress
# 147.229.2.90   or 17.0.0.1
#
dbinfo = geolite2.get_info()
print("dbinfo:", dbinfo)
#
input("Wait until key pressed")
#
ipaddr = ipaddress.ip_address("147.229.2.90")
print(ipaddr)
print(type(ipaddr))
match = geolite2.lookup(ipaddr)
#
print("Before Try")
try:
    print("Before Lookup in Try")
    ipaddr = ipaddress.ip_address("147.229.2.90")
    print(ipaddr)
    print(type(ipaddr))
    match = geolite2.lookup(ipaddr)
    if match == None:
        print("IP address lookup returned NONE")
    else:
        print("IP address lookup returned a MATCH")
    #
    print("After lookup")
except Exception as inst:
    print("Error found :", inst)
else:
    print("match.country:",      match.country)
    print("match.continent:",    match.continent)
    print("match.timezone:",     match.timezone)
    print("match.subdivisions:", match.subdivisions)
#                                                                                                                                                                                                                                                                                                                                                                         
#
input("Press enter to continue")
#
# If you want to use your own MaxMind database
# (for instance because you paid for the commercial version)
# you can open the database yourself:
#
from geoip import open_database
with open_database('data/GeoLite2-City.mmdb') as db:
    match = db.lookup_mine()
    print ('My IP info:', match.country)
#
print("End")
#
