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
    print ("scanurl:", scanurl)
    fullurl = apiurl +  scanurl
    print("fullurl:", fullurl)
    print("headers:", headers)
    response = requests.get(fullurl, params='', headers=headers, timeout=20)
    if debug:
        print("type(response):", type(response) )
    all_json = response.json()
    if debug:
        print("type(all_json):", type(all_json))
        print(json.dumps(all_json, indent=4, sort_keys=True) )
        print("===========================================")
    score = all_json["score"]
    if debug:
        print("type(score):", type(score) )
    print("score:"      , score )
    geography = all_json["geo"]
    if debug:
        print("type(geography):", type(geography) )
    print("geography:"      , geography )
    country = geography["country"]
    if debug:
        print("type(country):", type(country) )
    print("country:"      , country )
    country_code = geography["countrycode"]
    if debug:
        print("type(country_code):", type(country_code) )
    print("country_code:"      , country_code )
    cats = all_json["cats"]
    print("cats:"  , cats )
    cats_malware  =           get_cats(cats,"Malware")
    print("cats_malware:",    cats_malware )
    cats_spam     =           get_cats(cats,"Spam")
    print("cats_spam:",       cats_spam)
    cats_dynIP    =           get_cats(cats,"Dynamic IPs")
    print("cats_dynIP:",      cats_dynIP)
    cats_bots     =           get_cats(cats,"Bots")
    print("cats_bots:",       cats_bots)
    cats_anon_serv =          get_cats(cats,"Anonymisation Services")
    print("cats_anon_serv:",  cats_anon_serv)
    cats_scanning_IP =        get_cats(cats,"Scanning IPs")
    print("cats_scanning_IP:", cats_scanning_IP)
    cats_botnet_C2C =          get_cats(cats,"Botnet Command and Control Server")
    print("cats_botnet_c2c:",  cats_botnet_C2C)
    print("===========================================")
#
scanurl = "197.153.35.97"
apiurl = url + "/ipr/"
send_request(apiurl, scanurl, headers)
#
scanurl = "143.95.249.234"
apiurl = url + "/ipr/"
send_request(apiurl, scanurl, headers)
#
scanurl = "81.171.22.4"
apiurl = url + "/ipr/"
send_request(apiurl, scanurl, headers)
#
scanurl = "95.57.49.150"
apiurl = url + "/ipr/"
send_request(apiurl, scanurl, headers)
#
# apiurl = url + "/ipr/history/"
# send_request(apiurl, scanurl, headers)
# apiurl = url + "/ipr/malware/"
# send_request(apiurl, scanurl, headers)
#
print("The End")
#