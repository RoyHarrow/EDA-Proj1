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
print("Newar the End")
print("End")
#
