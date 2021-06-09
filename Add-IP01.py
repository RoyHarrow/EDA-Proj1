# Python Program to classify an IP address
#
# Potential subroutines to use
#
# 1.  ip2geotools
#
#     https://pypi.org/project/ip2geotools/
#
#     $ pip3 install requests --upgrade
#     $ pip3 install ip2geotools
#
from ip2geotools.databases.noncommercial import DbIpCity
response = DbIpCity.get('147.229.2.90', api_key='free')
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
