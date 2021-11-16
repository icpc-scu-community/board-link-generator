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
        "slashtag": "newcomersboardv1",    
        "title": "Newcomers Board"
    }
    requestHeaders = {
        "Content-type": "application/json",
        "apikey": "237fe9d5beff49c6b5d4a9c137870679",
        "workspace": "7a763333653b4d4ab7553bc868171fd4"
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
