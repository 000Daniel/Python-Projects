#!/usr/bin/python3
import argparse
import sys
import math

        #this error message appears when the formula cannot be solved.
def error_msg():
    print ("ERROR! this equation couldn't be solved!")
    quit()

        #this gets all the data from the command that is written in the terminal.
parser = argparse.ArgumentParser(description="Quadratic Formula - solutions.")
parser.add_argument('parameter_a', nargs='?' , type=float, help="a*X^2	pass a number(a) into the script")
parser.add_argument('parameter_b', nargs='?' , type=float, help="b*X	pass a number(b) into the script")
parser.add_argument('parameter_c', nargs='?' , type=float, help="c		pass a number(c) into the script2")

        #this converts said data to something we could use.
if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])

    if not args.parameter_a:
        error_msg()
    if not args.parameter_b:
        args.parameter_b = 0
    if not args.parameter_c:
        args.parameter_c = 0

        #calculates whether the equation could be solved or not.
        #if 'b4rootNum' is below 0 this equation cannot be solved.
b4rootNum = math.pow(args.parameter_b,2) - (4*args.parameter_a*args.parameter_c)
if b4rootNum >= 0:
    rootNum = math.sqrt(b4rootNum)      #this number is the outcome of the root in the equation.
else:
    error_msg()

        #the rest of the equation...
firstOption = ((-args.parameter_b) + rootNum) / (2*args.parameter_a)
secondOption = ((-args.parameter_b) - rootNum) / (2*args.parameter_a)
        #print the result.
print ("Output:\n ",firstOption,"\n ",secondOption)