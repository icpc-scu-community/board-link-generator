import json
import os
import requests
import sys
from helpers.colors import bcolors
import requests
import json
from dotenv import load_dotenv
load_dotenv()

def shortenLink(Link):
    print("Generating short url..\n\n")
    
    
    linkRequest = {
        "destination": Link,
        "domain": { "fullName": "rebrand.ly" },
        "slashtag": "",    
        "title": "Newcomers Board"
    }
    requestHeaders = {
        "Content-type": "application/json",
        "apikey": os.getenv('rebrandly_api_key'),
        "workspace": os.getenv('rebrandly_work_space_id')
    }

    while True:

        slashtag = input('Enter your slashtag: ')
        linkRequest['slashtag'] = slashtag
        try:
            r = requests.post("https://api.rebrandly.com/v1/links", data = json.dumps(linkRequest), headers = requestHeaders)
        except Exception as e:
            sys.exit(f"\nSomething went wrong with rebrandly api!\n {e}")
        
        if r.status_code == requests.codes.ok:
                link = r.json()
                break
        
        if r.status_code == 401:
            sys.exit(f"\n{bcolors.WARNING}Something went wrong with rebrandly api!\n")
        
        print('Try another slagtag because this one is used before\n')
        
        
    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    return link["shortUrl"]
