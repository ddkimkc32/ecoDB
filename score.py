#Score-calculating algorithm

'''
My plan is to take input a few factors and form a geometric mean of the value out of 1000

Factors:
    - Electric Bill 126
    - Gas Bill 62
    - Oil Bill 120
    - Yearly car mileage 14263
    - Number of flights
        - Short 2
        - Long 1
    - Do you recycle newspaper N
    - Do you recycle aluminum and tin N
'''

def calculateScore(electric, gas, oil, mileage, shortFlights, longFlights, newspaper, aluminum):
    total = 0
    electric *= 105
    gas *= 105
    oil *= 113
    mileage *= .79
    shortFlights *= 1100
    longFlights *= 4400
    if newspaper == False:
        total += 184
    if aluminum == False:
        total += 166
    total = electric + gas + oil + mileage + shortFlights + longFlights
    return total

def checkScore(score):
    if score < 6000:
        return "Very Low"
    elif score >= 6000 and score < 16000:
        return "Low"
    elif score >= 16000 and score < 22000:
        return "Average"
    else:
        return "High"

def mockUserInput():
    newspaper = True
    aluminum = True

    electric = int(input("Enter in your monthly electric bill: "))
    gas = int(input("Enter in your monthly gas bill: "))
    oil = int(input("Enter in your monthly oil heating bill: "))
    mileage = int(input("Enter in your total yearly mileage on your car: "))
    short = int(input("Enter in the number of short flights you take a year (4 hours or less): "))
    long = int(input("Enter in the number of long flights you take a year (more than 4 hours): "))
    newspaperResponse = input("Do you recycle newspaper? (Y/N)")
    aluminumResponse = input("Do you recycle aluminmum? (Y/N)")
    if newspaperResponse == "Y":
        newspaper = True
    else:
        newspaper = False

    if aluminumResponse == "Y":
        aluminum = True
    else:
        aluminum = False
    print(calculateScore(electric, gas, oil, mileage, short, long, newspaper, aluminum))

mockUserInput()
