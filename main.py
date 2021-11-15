import os
import json
from helpers.trainees import getTrainees
from helpers.groups import getGroups
from services.jsonbin import generateBin
from services.bitly import shortenLink
from helpers.colors import bcolors

def main():
    print(f"{bcolors.HEADER}Welcome to Board link generator!{bcolors.ENDC}")

    board = {
        'groups': getGroups(), 
        'trainees': getTrainees(),
    }

    
    with open('output.json', 'w+') as output_file:
        output_file.write(json.dumps(board))

    print(f"{bcolors.HEADER}Json data successfully created in output.json{bcolors.ENDC}")

    if not 'jsonbin_api_key' in os.environ:
        print(f"{bcolors.WARNING}bin will not be created. If you want to create a jsonbin, please specify jsonbin (api key) inside env file.")
        return 
    
    jsonbin_url = generateBin(board)
    board_url = 'https://boardy.cf/?configs={}'.format(jsonbin_url)

    print(f"{bcolors.OKGREEN}\nBoard successfully generated with the following link:")
    print(f"{bcolors.HEADER}{board_url}\n{bcolors.ENDC}")

    with open('links.txt', 'w+') as links_file:
        links_file.write(f"jsonbin url: {jsonbin_url}\n")
        links_file.write(f"Full board url: {board_url}\n")

        if not 'bitly_api_key' in os.environ:
            print(f"{bcolors.WARNING}Link will not be shorten. If you want to shorten the link please specify bitly (api key) inside env file.")
            return
        
        shorten_url = shortenLink(board_url)
        print(f"{bcolors.OKGREEN}\nShorten url successfully generated with the following link:")
        print(f"{bcolors.HEADER}{shorten_url}")

        links_file.write(f"Shorten url: {shorten_url}")
        

if __name__ == "__main__":
    main()

