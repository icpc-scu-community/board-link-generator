from helpers.colors import bcolors
import sys
import csv

def getTraineesData():
    result = []
    with open("data/trainees.csv") as trainees_file:
        csv_reader = csv.reader(trainees_file, delimiter=',')
        
        headers = True
        for row in csv_reader:
            if headers:
                headers = False
                continue
            result.append({'name': row[0].strip(), 'handle': row[1].strip()})
    return result

def getTrainees():
    print("Parsing trainees..", sep="   ")
    
    try:
        result = getTraineesData()
    except:
        sys.exit("Please provide trainees.csv inside data folder")
    

    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    return result
