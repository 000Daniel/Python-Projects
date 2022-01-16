#!/usr/bin/python3
import argparse
import math
import time
import os
startTime = time.time()

                            #these lines get the launch options of this script
parser = argparse.ArgumentParser(description="created by https://github.com/000Daniel")
parser.add_argument('maxvalue', type=int, metavar='', nargs='?', help="pass a number into the script")
parser.add_argument('-q', '--quiet', action='store_true',help='don\'t print any results')
parser.add_argument('-s', '--sort', action='store_true',help='sort the numbers (slow)')
parser.add_argument('-f', '--file', action='store_true',help='store the result into a local file')
args = parser.parse_args()  #converts the flag data into usable data

                            #the script checks if the user entered a value
                            #and fixes it to a positive one
if not args.maxvalue:
    print("Error! please enter a valie")
    quit()
if args.maxvalue < 0:
    args.maxvalue = args.maxvalue * (-1)

                            #these Lists will contain all of the numbers necessary
PrimeList = []
NonPrimeList = []
sqrtMaxValue = math.sqrt(args.maxvalue)

                            #for every number from 1 to 'chosen value' run:
for x in range(1,args.maxvalue + 1):
    skipCheck = 0
    numOfSuccess = 0
                            #check if number('x') already exists in the PrimeList,
                            #if it does set 'skipCheck' to 1 so we won't calculate it.
                            #'skipCheck' resets for each number('x')
    for s in PrimeList:
        if (s > x):
            break
        if (x == s):
            skipCheck = 1
                            
    if (skipCheck == 0):
                            #this 'for loop' makes sure the script won't check a number it doesn't have to.
                            #for every number from 2 to 'x' run:
        for y in range(2,x):
                            #if a number was divided without any remainders add 1 Success.
                            #'numOfSuccess' resets for each number('x')
            if not x % y:
                numOfSuccess += 1
        
                            #if 'numOfSuccess' is atleast 2 add the number('x') to PrimeList, because it was
                            #divided atleast once(not including by 1) without any remainders.
        if numOfSuccess >= 2:
            PrimeList.append(x)
                            #else add that number to NonPrimeList.
                            #Non-prime * Non-prime = prime
                            #output a squared NonPrime, converts it to an int(removes .0 remainder), and add
                            #it to PrimeList.
        else:
            NonPrimeList.append(x)
        if (x <= sqrtMaxValue):
            squaredNonPrime = x * x
            PrimeList.append(int(squaredNonPrime))

                            #if the user wrote '-s' sort both Lists.
if args.sort:
    NonPrimeList.sort()
    PrimeList.sort()

                            #if the user wrote '-q' don't print anything.
                            #useful for a faster '-f' option.
if not args.quiet:
    print("Non Prime Numbers:")
    print(NonPrimeList)
    print("Prime Numbers:")
    print(PrimeList)

                            #if the user wrote '-f' delete the 'existing' files and create new ones with
                            #the relevant data inside.
if args.file:
    if os.path.exists("total-Prime-numbers.txt"):
        os.remove("total-Prime-numbers.txt")
    if os.path.exists("total-NonPrime-numbers.txt"):
        os.remove("total-NonPrime-numbers.txt")

    with open("total-Prime-numbers.txt", "x") as f:
        f.write(str(PrimeList))
    with open("total-NonPrime-numbers.txt", "x") as f:
        f.write(str(NonPrimeList))

                            #print how long the script executed for.
executionTime = (time.time() - startTime)
print("Execution time in seconds: " + str(executionTime))
#created by https://github.com/000Daniel