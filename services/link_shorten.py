import json
import os
import sys
from helpers.colors import bcolors
import requests
import urllib
import json
from dotenv import load_dotenv
load_dotenv()


def getResponseMessage(status):
    switcher = [
        "Unknown error"
        f"\n{bcolors.WARNING}the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened\n",
        f"\n{bcolors.WARNING}the entered link is not a link\n",
        "Unknown error",
        f"\n{bcolors.WARNING}Invalid API key\n",
        f"\n{bcolors.WARNING}the link has not passed the validation. Includes invalid characters\n",
        f"\n{bcolors.WARNING}The link provided is from a blocked domain\n",
    ]
    return switcher[status]


def shortenLink(Link):
    if not 'cuttly_api_key' in os.environ:
        print(f"{bcolors.WARNING}Link will not be shorten. If you want to shorten the link please specify cuttly (api key) inside env file.")
        sys.exit()

    print("\nGenerating short url..\n")

    while True:

        slashtag = input("Enter url's slashtag: ")

        key = os.getenv('cuttly_api_key')
        url = urllib.parse.quote(Link)
        name = slashtag

        try:
            r = requests.get(
                'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
        except Exception as e:
            sys.exit(f"\nSomething went wrong with rebrandly api!\n {e}")

        json_response = r.json()['url']
        response_status = json_response['status']
        if response_status == 7:
            print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
            break
        elif response_status != 3:
            sys.exit(getResponseMessage(response_status))

        print(
            f"{bcolors.WARNING}Sorry, this slashtag is used!{bcolors.ENDC}")

    print(f"{bcolors.OKYELLOW}\nShorten url successfully generated with the following link:")
    print(f"{bcolors.OKBLUE}{json_response['shortLink']}")
    return json_response['shortLink']

