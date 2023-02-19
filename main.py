import json

from dotenv import load_dotenv

from helpers.colors import bcolors
from helpers.groups import getGroups
from helpers.trainees import getTrainees
from services.json_uploader import generateBin
from services.link_shorten import shortenLink

load_dotenv()


def saveToFile(fileName, mode, data):
    with open(f"{fileName}", mode) as file:
        file.write(data)


def getBoardData():
    return {
        "groups": getGroups(),
        "trainees": getTrainees(),
    }


def getFullBoardUrl(json_url):
    board_url = "https://boardy.tk/?configs={}".format(json_url)
    print(f"{bcolors.OKYELLOW}\nBoard successfully generated with the following link:")
    print(f"{bcolors.OKBLUE}{board_url}\n{bcolors.ENDC}")
    return board_url


def main():

    print(f"{bcolors.HEADER}Welcome to Board link generator!\n{bcolors.ENDC}")

    # creating dictionary of required board's data
    board = getBoardData()

    # saving board data as json in board.json.
    saveToFile("board.json", "w", json.dumps(board))

    print(
        f"{bcolors.OKYELLOW}\nJson data successfully created in board.json{bcolors.ENDC}"
    )

    # generating bin for board's json
    json_bin_url = generateBin(board)

    # getting the full url for boardy.tk using configs queryString.
    full_board_url = getFullBoardUrl(json_bin_url)

    # saving jsonbin link and full board url in links.txt.
    saveToFile(
        "links.txt",
        "w+",
        f"jsonbin url: {json_bin_url}\nFull board url: {full_board_url}\n",
    )

    while True:
        option = input("Do you want to shorten the board's link? (y/n): ")
        if option.lower() == "y" or option.lower() == "n":
            break
        else:
            print(f"{bcolors.WARNING}Please enter y or n ... \n{bcolors.ENDC}")

    if option.lower() == "y":
        # generating shorturl to the full board url
        shorten_url = shortenLink(full_board_url)
        # saving the shorten url in links.txt.
        saveToFile("links.txt", "a", f"Shorten url: {shorten_url}\n")


if __name__ == "__main__":
    main()
