import random

def insert(listofvalues):
    print("write your code of insert here.\n")

def insertionsort (listofvalues):
    print("use insert function to sort the list.\n")

def runinsertionsort():
    numbers=int(input("Enter N \n"))
    values = []
    for i in range(0,numbers):
        n = random.randint(1,300)
        values.append(n)
    insertionsort(values)
    print(values)


def movemin(listofValues,indextostart):
    print("write code to implement movemin\n")

def selectionsort(listofvalues):
    print("write code to implement selectionsort using movemin function\n")

def runselectionsort():
    numbers=int(input("Enter N \n"))
    values = []
    for i in range(0,numbers):
        n = random.randint(1,300)
        values.append(n)
    selectionsort(values)
    print(values)
