import os
import requests
import sys
from helpers.colors import bcolors


def generateBin(data):
    if not 'jsonbin_api_key' in os.environ:
        print(f"{bcolors.WARNING}bin will not be created. If you want to create a jsonbin, please specify jsonbin (api key) inside env file.")
        sys.exit()

    print("\nGenerating bin link..")
    url = 'https://api.jsonbin.io/v3/b'
    headers = {
        'Content-Type': 'application/json',
        'X-Master-Key': os.getenv('jsonbin_api_key'),
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
    
    print(f"{bcolors.OKGREEN}ACCEPTED!\n{bcolors.ENDC}")

    print(f"{bcolors.OKYELLOW}Your board's bin link is: {bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}{jsonbin_url}{bcolors.ENDC}")
    
    return jsonbin_url
