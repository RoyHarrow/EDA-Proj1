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
match = geolite2.lookup('17.0.0.1')
# match is not None
# True
print("match.country:",      match.country)
print("match.continent:",    match.continent)
print("match.timezone:",     match.timezone)
print("match.subdivisions:", match.subdivisions)
#                                                                                                                                                                                                                                                                                                                                                                         
#frozenset(['CA'])
#
#
#
# If you want to use your own MaxMind database
# (for instance because you paid for the commercial version)
# you can open the database yourself:
#
with open_database('data/GeoLite2-City.mmdb') as db:
    match = db.lookup_mine()
    print 'My IP info:', match
#
# Geolite - https://dev.maxmind.com/geoip#geolite-databases-and-services
#

#
from ip2geotools.databases.noncommercial import DbIpCity
ipAddr = "147.229.2.90"
#ipAddr = "253.253.253.253"
#ipAddr = "2001:4451:446d:3300:7085:c68a:2252:bbb1"
try:
    response = DbIpCity.get(ipAddr, api_key='free')
except Exception as inst:
    print("Error found :", inst)
else:
    print ("response.ip_address:", response.ip_address)
    print ("response.city:",       response.city )
    print("response.region:",      response.region )
    print("response.country:",     response.country )
    print("response.latitude:",    response.latitude )
    print("response.longitude:",   response.longitude )
    # print("response.to_json():,    response.to_json() )
    # print("response.to_xml():",    response.to_xml() )
#
print("End")
#
#
#     https://pypi.org/project/ip2geotools/
#
#     $ pip3 install requests --upgrade
#     $ pip3 install ip2geotools
#
from ip2geotools.databases.noncommercial import DbIpCity
ipAddr = "147.229.2.90"
#ipAddr = "253.253.253.253"
#ipAddr = "2001:4451:446d:3300:7085:c68a:2252:bbb1"
try:
    response = DbIpCity.get(ipAddr, api_key='free')
except Exception as inst:
    print("Error found :", inst)
else:
    print ("response.ip_address:", response.ip_address)
    print ("response.city:",       response.city )
    print("response.region:",      response.region )
    print("response.country:",     response.country )
    print("response.latitude:",    response.latitude )
    print("response.longitude:",   response.longitude )
    # print("response.to_json():,    response.to_json() )
    # print("response.to_xml():",    response.to_xml() )
#
print("End")
#
