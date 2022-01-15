#!/usr/bin/python3
import argparse
from xml.etree.ElementTree import tostring

                            #these lines get the launch options of this script
parser = argparse.ArgumentParser(description="created by https://github.com/000Daniel")
parser.add_argument('minvalue', type=int, metavar='', nargs='?', help="pass a string into the script")
parser.add_argument('maxvalue', type=int, metavar='', nargs='?', help="pass a string into the script")
args = parser.parse_args()  #converts the flag data to something usable in script

                            #in these lines the script checks if the user wrote both values
if not args.minvalue or not args.maxvalue:
    print("Error! please enter a valie")
    quit()

                            #this function swaps minvalue with maxvalue if:
                            #maxvalue is smaller than minvalue
def sortMinToMax():
    if args.maxvalue < args.minvalue:
        args.maxvalue += args.minvalue
        args.minvalue = args.maxvalue - args.minvalue
        args.maxvalue -= args.minvalue

sortMinToMax()
print("Those are the values:\nmin: " + str(args.minvalue) +"\nmax: " + str(args.maxvalue))

                            #these two 'if' statements would convert negative values
                            #to positive ones.
if args.minvalue < 0:
    args.minvalue = args.minvalue * (-1)

if args.maxvalue < 0:
    args.maxvalue = args.maxvalue * (-1)

sortMinToMax()

                            #this 'for loop' would try to divide every number from 1 to
                            #minvalue both minvalue and maxvalue.
                            #every time that this 'for loop' gets two values that divided
                            #both the min and max values without a remainder, it will
                            #store that as the value for 'result'.
                            #this way at the end of the loop, the script will output the
                            #highest value possible that can divide between both min and
                            #max values without any remainders.
result = None
for i in range(1,args.minvalue + 1):
    if not args.minvalue % i and not args.maxvalue % i:
            result = i
            

print(str(result) + " is the highest number that can divide both values without remainders")
#created by https://github.com/000Daniel