import json
import os
from requests.api import head
from helpers.trainees import getTrainees
from helpers.groups import getGroups
from services.json_uploader import generateBin
from services.link_shorten import shortenLink
from helpers.colors import bcolors
from dotenv import load_dotenv
load_dotenv()

def saveToFile(fileName, data):
    with open(f'{fileName}', 'w+') as file:
        file.write(data)


def getBoardData():
    return {
        'groups': getGroups(),
        'trainees': getTrainees(),
    }

def getFullBoardUrl(json_url):
    board_url = "https://boardy.cf/?configs={}".format(json_url)
    print(f"{bcolors.OKYELLOW}\nBoard successfully generated with the following link:")
    print(f"{bcolors.OKBLUE}{board_url}\n{bcolors.ENDC}")
    return board_url


def main():
        
    print(f"{bcolors.HEADER}Welcome to Board link generator!\n{bcolors.ENDC}")
    
    # creating dictionary of required board's data 
    board =  getBoardData()
    
    # saving board data as json in board.json.
    saveToFile('board.json', json.dumps(board))
    
    print(f"{bcolors.OKYELLOW}\nJson data successfully created in board.json{bcolors.ENDC}")
    
    # generating bin for board's json
    json_bin_url = generateBin(board)
    
    # getting the full url for boardy.cf using configs queryString.
    full_board_url = getFullBoardUrl(json_bin_url)
    
    # saving jsonbin link and full board url in links.txt.
    saveToFile('links.txt', f"jsonbin url: {json_bin_url}\nFull board url: {full_board_url}\n")
    
    # generating shorturl to the full board url
    shorten_url = shortenLink(full_board_url)
    
    # saving the shorten url in links.txt.
    saveToFile('links.txt', f"Shorten url: {shorten_url}\n")

         
if __name__ == "__main__":
    main()
