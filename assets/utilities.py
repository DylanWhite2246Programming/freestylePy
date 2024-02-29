import csv
import assets.constants as cons

def oz2ml(oz):
    return 29.574*oz

def ml2oz(ml):
    return ml/29.574

def readBalance(name):
    with open(cons.USERS_CSV_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == name:
                return row[2]
            else:
                return 0

global cUser 
cUser = ''        
def getCurrentUser():
    return cUser

def setUser(user):
    cUser = user
    