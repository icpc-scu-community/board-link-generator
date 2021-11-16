import requests
import sys
from helpers.colors import bcolors
import requests
import json

def shortenLink(Link):
    print("Generating short url..")
    
    linkRequest = {
        "destination": Link,
        "domain": { "fullName": "rebrand.ly" },
        "slashtag": "Newcomers_Boards",    
        "title": "Newcomers Board"
    }
    requestHeaders = {
        "Content-type": "application/json",
        "apikey": "Your_api_key",
        "workspace": "Your_WorkSpace_id"
    }

    r = requests.post("https://api.rebrandly.com/v1/links", data = json.dumps(linkRequest), headers = requestHeaders)

    if (r.status_code == requests.codes.ok):
        link = r.json()
    else:
        print(f"{bcolors.WARNING}Something went wrong with rebrandly.")
        print(f"{bcolors.FAIL}Error message: {r['message']}") 
        sys.exit() 
        
    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    return link["shortUrl"]
