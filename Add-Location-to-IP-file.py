## Read Combined IP address file into a list and add location info. from ip address ##
#
import pandas as pd
#
from ip2geotools.databases.noncommercial import DbIpCity
#
response = DbIpCity.get('147.229.2.90', api_key='free')
print ("response.ip_address:", response.ip_address)
print ("response.city:",       response.city )
print("response.region:",      response.region )
print("response.country:",     response.country )
print("response.latitude:",    response.latitude )
print("response.longitude:",   response.longitude )
#
print ("Reading a CSV file into a Data Frame")
#
csv_path = "Combined_Subset.csv"
csv_path = "Combined.csv"
#
# Using Data Frames
#
csvDF = pd.read_csv(csv_path)
#
# The the data frame method "head" reads the first 5 records of the file
#
# df.head()
#
print("type(csvDF) = ", type(csvDF) )
#
print("csvDF       = \n", csvDF       )
#
print ("===========================")
#
print("Number of Rows:", len(csvDF) )
#
print ("===========================")
#
# Add empty columns
#
csvDF["City"]           = ""
csvDF["Region"]         = ""
csvDF["Country"]        = ""
csvDF["Latitude"]       = 0.0
csvDF["Longitude"]      = 0.0
#
print("csvDF       = \n", csvDF       )
#
print ("===========================")
#
for i in range(len(csvDF) ):
    ipAddr = csvDF.loc[i,"IP Address"]
    print(i, ipAddr)
    #
    try:
        response = DbIpCity.get(ipAddr, api_key='free')
    except Exception as inst:
        print("Error raised for row:", i, inst)
    else:
        print("response.ip_address:", response.ip_address)
        print("response.city:",       response.city )
        print("response.region:",     response.region )
        print("response.country:",    response.country )
        print("response.latitude:",   response.latitude )
        print("response.longitude:",  response.longitude )
        csvDF.loc[i,"City"]         = response.city
        csvDF.loc[i,"Region"]       = response.region
        csvDF.loc[i,"Country-Code"] = response.country
        csvDF.loc[i,"Latitude"]     = response.latitude
        csvDF.loc[i,"Longitude"]    = response.longitude
#
print("csvDF       = \n", csvDF       )
#
# Write updated file out from Pandas Dataframe
#
out_path = "Combined_Subset2.csv"
out_path = "Combined_Data.csv"
#
csvDF.to_csv(out_path,index=False)
#
#
print("END")