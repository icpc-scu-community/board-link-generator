import json
import os
from requests.api import head
from helpers.Trainees import Get_Trainees
from helpers.Groups import Get_Groups
from Service.jsonbin import generateBin
from Service.rebrandly import shortenLink
from helpers.colors import bcolors

def main():
    
    os.environ['jsonbin_api_key'] = "Your_jsonbin_abi_key"
    os.environ['rebrandly_api_key'] = "Your_rebrandly_api_key"
    
    print(f"{bcolors.HEADER}Welcome to Board link generator!\n{bcolors.ENDC}")
    Board = {
        "groups" : Get_Groups(),
        "trainees" : Get_Trainees()
    }
    
    with open('Board.json', 'w+') as output_file:
        output_file.write(json.dumps(Board))
   
    print(f"{bcolors.OKYELLOW}\nJson data successfully created in Board.json{bcolors.ENDC}")
    
    if not 'jsonbin_api_key' in os.environ:
        print(f"{bcolors.WARNING}bin will not be created. If you want to create a jsonbin, please specify jsonbin (api key) inside env file.")
        return
    
    json_bin_url = generateBin(Board)
    
    Board_url = "https://boardy.cf/?configs={}".format(json_bin_url)
    
    print(f"{bcolors.OKYELLOW}\nBoard successfully generated with the following link:")
    print(f"{bcolors.OKBLUE}{Board_url}\n{bcolors.ENDC}")
    
    if not 'rebrandly_api_key' in os.environ:
            print(f"{bcolors.WARNING}Link will not be shorten. If you want to shorten the link please specify rebrandly (api key) inside env file.")
            return    
    
    shorten_url = shortenLink(Board_url)
    
    print(f"{bcolors.OKYELLOW}\nShorten url successfully generated with the following link:")
    print(f"{bcolors.OKBLUE}{shorten_url}")
    
    with open('links.txt', 'w+') as links_file:
        links_file.write(f"jsonbin url: {json_bin_url}\n")
        links_file.write(f"Full board url: {Board_url}\n")
        links_file.write(f"Shorten url: {shorten_url}\n")
         
if __name__ == "__main__":
    main()
