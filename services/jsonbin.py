import os
import requests
import sys
from helpers.colors import bcolors

def generateBin(data):
    print("\nGenerating bin link..")
    url = 'https://api.jsonbin.io/v3/b'
    
    headers = {
    'Content-Type': 'application/json',
    'X-Master-Key': os.environ['jsonbin_api_key'],
    'X-Bin-Private': 'false',
    }

    try:
        req = requests.post(url, json=data, headers=headers)
    except Exception as e:
        print(f"{bcolors.WARNING}Something went wrong with jsonbin!")
        print(e)
        sys.exit()

    jsonbin = req.json()
    if not req.ok:
        print(f"{bcolors.WARNING}Something went wrong with jsonbin.")
        if 'message' in jsonbin:
            print(f"{bcolors.FAIL}Error message: {jsonbin['message']}") 
        sys.exit() 
    
    jsonbin_url = 'https://api.jsonbin.io/b/{}'.format(jsonbin['metadata']['id'])
    
    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")

    print(f"{bcolors.HEADER}Your board's bin link is: {jsonbin_url}{bcolors.ENDC}")
    return jsonbin_url
