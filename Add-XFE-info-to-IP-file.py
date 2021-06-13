# Python Program to retrieve X-Force Exchange information for an IP address
#
import requests
import json
import base64
#
debug = False
#
key      = bytes(b"141180ec-9973-42e3-8186-7b08a4b4531b") # https://exchange.xforce.ibmcloud.com/settings/api
password = bytes(b"67a434cb-c157-4809-a415-c5c9d1d7701a")
#
token = str(base64.b64encode(key + b":" + password) )
if debug:
    print("type(token):", type(token) )
    print("token:",       token)
tok_str = token[2:-1]
if debug:
    print("type(tok_str):", type(tok_str) )
print("tok_str:",       tok_str)
headers = {'Authorization': "Basic " + tok_str, 'Accept': 'application/json'}
url = "https://api.xforce.ibmcloud.com:443"
print("===========================================")
#
def get_cats(cats_dict_in, category_in):
    try:
        cats_value   =  cats_dict_in[category_in]
    except Exception as excep:
        if debug:
            print ("Error in get_cats:", excep)
        cats_value=0
    finally:
        if debug:
            print("cats_value:"  , cats_value )
    return(cats_value)
#
def send_request(apiurl, scanurl, headers):
    #
    # Declare global variables for results from XFE API call
    #
    global score            
    global country          
    global country_code     
    global cats_malware     
    global cats_spam        
    global cats_dynIP       
    global cats_bots        
    global cats_anon_serv   
    global cats_scanning_IP 
    global cats_botnet_C2C  
    global cats_scanning_IP 
    global cats_botnet_C2C  
    #
    score            = 0.0
    country          = ""
    country_code     = ""
    cats_malware     = 0
    cats_spam        = 0
    cats_dynIP       = 0
    cats_bots        = 0
    cats_anon_serv   = 0
    cats_scanning_IP = 0
    cats_botnet_C2C  = 0
    cats_scanning_IP = 0
    cats_botnet_C2C  = 0
    #
    print ("scanurl:", scanurl)
    fullurl = apiurl +  scanurl
    print("fullurl:", fullurl)
    print("headers:", headers)
    try:
        response = requests.get(fullurl, params='', headers=headers, timeout=20)
        if debug:
            print("type(response):", type(response) )
    except Exception as inst:
        print("Error: " + inst + "  URL: " + fullurl)
    else:
        all_json = response.json()
        if debug:
            print("type(all_json):", type(all_json))
            print(json.dumps(all_json, indent=4, sort_keys=True) )
            print("===========================================")
        score = all_json["score"]
        if debug:
            print("type(score):", type(score) )
        print("score:"      , score )
        try:
            geography = all_json["geo"]
        except:
            geography = ""
        finally:
            if debug:
                print("type(geography):", type(geography) )
            print("geography:"      , geography )
        #
        try:
            country = geography["country"]
        except:
            country = ""
        finally:
            if debug:
                print("type(country):", type(country) )
            print("country:"      , country )
        #
        try:
            country_code = geography["countrycode"]
        except:
            if country == "Hong Kong S.A.R. of China":
                country_code = "CN"
            else:
                country_code = ""
        finally:
            if debug:
                print("type(country_code):", type(country_code) )
            print("country_code:"      , country_code )
        #
        cats = all_json["cats"]
        print("cats:"  , cats )
        cats_malware  =            get_cats(cats,"Malware")
        print("cats_malware:",     cats_malware )
        cats_spam     =            get_cats(cats,"Spam")
        print("cats_spam:",        cats_spam)
        cats_dynIP    =            get_cats(cats,"Dynamic IPs")
        print("cats_dynIP:",       cats_dynIP)
        cats_bots     =            get_cats(cats,"Bots")
        print("cats_bots:",        cats_bots)
        cats_anon_serv =           get_cats(cats,"Anonymisation Services")
        print("cats_anon_serv:",   cats_anon_serv)
        cats_scanning_IP =         get_cats(cats,"Scanning IPs")
        print("cats_scanning_IP:", cats_scanning_IP)
        cats_botnet_C2C =          get_cats(cats,"Botnet Command and Control Server")
        print("cats_botnet_c2c:",  cats_botnet_C2C)
        #
    print("===========================================")
#
print("The Middle")
#
## Read Combined IP address file into a list and add info. from IBM X-Force Exchange using API calls ##
#
import pandas as pd
#
print ("Reading a CSV file into a Data Frame")
#
csv_path = "Combined_Subset.csv"
# csv_path = "Combined.csv"
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
csvDF["Country"]            = ""
csvDF["Country-Code"]       = ""
csvDF["XFE-Score"]          = 0.0
csvDF["XFE-Cat-Spam"]       = 0
csvDF["XFE-Cat-AnonServ"]   = 0
csvDF["XFE-Cat-ScanningIP"] = 0
csvDF["XFE-Cat-DynamicIP"]  = 0
csvDF["XFE-Cat-Malware"]    = 0
csvDF["XFE-Cat-Bots"]       = 0
csvDF["XFE-Cat-BotnetC2C"]  = 0
#
print("csvDF       = \n", csvDF       )
#
print ("===========================")
#
for i in range(len(csvDF) ):
    ipAddr = csvDF.loc[i,"IP Address"]
    print(i, ipAddr)
    #
    # country          = ""
    # country_code     = ""
    # score            = 0.0
    # cats_malware     = 0
    # cats_spam        = 0
    # cats_dynIP       = 0
    # cats_bots        = 0
    # cats_anon_serv   = 0
    # cats_scanning_IP = 0
    # cats_botnet_C2C  = 0
    # cats_scanning_IP = 0
    # cats_botnet_C2C  = 0
    #
    try:
        # response = DbIpCity.get(ipAddr, api_key='free')
        scanurl = ipAddr
        apiurl = url + "/ipr/"
        send_request(apiurl, scanurl, headers)
    except Exception as inst:
        print("Error raised for row:", i, inst)
    else:
        #if debug:
        print("ipAddr:",       ipAddr)
        print("country:",      country)
        print("country_code:", country_code)
        print("score:",        score)
        print("cats_spam:",    cats_spam)
        print("cats_bots:",    cats_bots)
        print("cats_malware:", cats_malware)
        print("cats_spam:",    cats_spam)
        csvDF.loc[i,"Country"]            = country
        csvDF.loc[i,"Country-Code"]       = country_code
        csvDF.loc[i,"XFE-Score"]          = score
        csvDF.loc[i,"XFE-Cat-Spam"]       = cats_spam
        csvDF.loc[i,"XFE-Cat-AnonServ"]   = cats_anon_serv
        csvDF.loc[i,"XFE-Cat-ScanningIP"] = cats_scanning_IP
        csvDF.loc[i,"XFE-Cat-DynamicIP"]  = cats_dynIP
        csvDF.loc[i,"XFE-Cat-Malware"]    = cats_malware
        csvDF.loc[i,"XFE-Cat-Bots"]       = cats_bots
        csvDF.loc[i,"XFE-Cat-BotnetC2C"]  = cats_botnet_C2C
#
print("csvDF       = \n", csvDF       )
#
# Write updated file out from Pandas Dataframe
#
out_path = "Combined_Subset2.csv"
# out_path = "Combined_Data.csv"
#
csvDF.to_csv(out_path,index=False)
#
#
print("END")