import requests
import sys
from helpers.colors import bcolors
import os

def shortenLink(link):
    print("Generating short url..")
    url = 'https://api-ssl.bitly.com/v4/bitlinks'

    data = {
        "domain": "bit.ly",
        "long_url": link
    }  
    headers = {"Authorization": f"Bearer {os.environ['bitly']}"}

    try:
        req = requests.post(url, json=data,headers=headers)
    except Exception as e:
        print(f"{bcolors.WARNING}Something went wrong with bitly.")
        print(e)
        sys.exit() 

    bitly = req.json()
    if not req.ok:
        print(f"{bcolors.WARNING}Something went wrong with bitly.")
        if 'message' in bitly:
            print(f"{bcolors.FAIL}Error message: {bitly['message']}") 
        sys.exit() 

    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    return bitly['link']