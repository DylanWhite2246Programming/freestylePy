import csv
import assets.constants as cons

def oz2ml(oz):
    return 29.574*oz

def ml2oz(ml):
    return ml/29.574

mlpershot = oz2ml(1.5)

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

def calculate_price(name, shots, amount):
    price = 0
    with open("assets/recipies/"+str(name).replace(" ","")+'.csv') as rfile:
        rreader = csv.reader(rfile)
        for rrow in rreader: 
            if rrow[2]=='true':
                with open('assets/sources.csv') as sfile:
                    sreader = csv.reader(sfile)
                    for srow in sreader:
                        if srow[0]==rrow[1]:
                            #price #amount #ratio
                            price += float(srow[3])*mlpershot*shots*float(rrow[0])
            if rrow[2]=='false':
                    with open('assets/sources.csv') as sfile:
                        sreader = csv.reader(sfile)
                        for srow in sreader:
                            if srow[0]==rrow[1]:
                                #price #ratio #mixer amount
                                price += float(srow[3])*float(rrow[0])*(oz2ml(amount)-(shots*mlpershot))
    return round(price,2)

def calculate_percentage(name, shots, amount):
    percentage = 0
    with open("assets/recipies/"+str(name).replace(" ","")+'.csv') as rfile:
        rreader = csv.reader(rfile)
        for rrow in rreader: 
            if rrow[2]=='true':
                with open('assets/sources.csv') as sfile:
                    sreader = csv.reader(sfile)
                    for srow in sreader:
                        if srow[0]==rrow[1]:
                            #percentage #ratio #amount
                            percentage += float(srow[4])*float(rrow[0])*shots*mlpershot
    return round(percentage/oz2ml(amount)*100,1)