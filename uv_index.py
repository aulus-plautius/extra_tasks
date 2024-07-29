import json
import requests

def check_postcode(postcode):
    file = open("postcodes.csv", "r")
    postcodes = file.readlines()
    file.close()
    for postcode_1 in postcodes:
        if postcode in postcode_1:
            return True
    else:
        return False
    
def get_lat_lng(postcode):
    if check_postcode(postcode):
        url = "https://api.postcodes.io/postcodes/"
        lat_lng = requests.get(url + postcode).json()
        lat = lat_lng["result"]["latitude"]
        lng = lat_lng["result"]["longitude"]
        return (lat, lng)
    else:
        return "Invalid Postcode!"
    
def get_uv_index():
    postcode = input("Give a postcode for the current uv: ")
    lat_lng = get_lat_lng(postcode)
    parameters = f"lat={lat_lng[0]}&lng={lat_lng[1]}&alt=100&dt="
    url = "https://api.openuv.io/api/v1/uv?"
    headers = {"x-access-token": "openuv-1csqorlz2tueco-io"}
    uv_data = requests.get(url+parameters, headers=headers).json()
    print(f"The current uv is {uv_data["result"]["uv"]}")

get_uv_index()

