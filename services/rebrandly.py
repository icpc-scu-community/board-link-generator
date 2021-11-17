import json
import os
import requests
import sys
from helpers.colors import bcolors
import requests
import json

def shortenLink(Link):
    if not 'rebrandly_api_key' in os.environ or not 'rebrandly_workspace_id' in os.environ:
        print(f"{bcolors.WARNING}Link will not be shorten. If you want to shorten the link please specify rebrandly (api key) inside env file.")
        sys.exit()

    print("Generating short url..\n\n")
    
    print(os.environ['rebrandly_workspace_id'])
    linkRequest = {
        "destination": Link,
        "domain": { "fullName": "rebrand.ly" },
        "slashtag": "",    
        "title": "Newcomers Board"
    }
    requestHeaders = {
        "Content-type": "application/json",
        "apikey": os.getenv('rebrandly_api_key'),
        "workspace": os.getenv('rebrandly_workspace_id')
    }

    while True:

        slashtag = input('Enter your slashtag: ')
        linkRequest['slashtag'] = slashtag
        try:
            r = requests.post("https://api.rebrandly.com/v1/links", data = json.dumps(linkRequest), headers = requestHeaders)
        except Exception as e:
            sys.exit(f"Something went wrong with rebrandly api!\n{e}")
        
        if r.status_code == requests.codes.ok:
                link = r.json()
                break
        
        if r.status_code == 401:
            sys.exit(f"Something went wrong with rebrandly api!\n{r.text}")
        
        print('Try another slagtag because this one is used before')
        
        
    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    
    print(f"{bcolors.OKYELLOW}\nShorten url successfully generated with the following link:")
    print(f"{bcolors.OKBLUE}{link['shortUrl']}")

    return link["shortUrl"]
