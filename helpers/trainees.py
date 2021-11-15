from helpers.colors import bcolors
import sys
import csv

def getTrainees():
    print("Parsing trainees..", sep="   ")

    try:
        trainees_file = open("data/trainees.csv")
    except IOError:
        print(f"{bcolors.FAIL}Please provide trainees.csv inside data folder")
        sys.exit()

    csv_reader = csv.reader(trainees_file, delimiter=',')

    result = []
    headers = True
    for row in csv_reader:
        if headers:
            headers = False
            continue
        result.append({'name': row[0].strip(), 'handle': row[1].strip()})
    
    trainees_file.close()

    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    return result
