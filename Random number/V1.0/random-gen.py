#!/usr/bin/python3
import argparse
import textwrap
import random

                    #these are the options that we can parse(pass) into this script.
parser = argparse.ArgumentParser(description='Random number and or string generator',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''\
         usage:
           random-gen.py 1 100        generate a random number between 1 and 100
           random-gen.py -s 100 50    generate a random character from 33 to 100(ASCII code), 50 times
           random-gen.py -s -1        generate a random character from 33 to 10000(ASCII code), 20 times(default)



           created by https://github.com/000Daniel
         '''))
parser.add_argument('option1', nargs='?', type=int, help='passes the first int into the script')
parser.add_argument('option2', nargs='?', type=int, help='passes the second int into the script')
parser.add_argument('-s', '--string', action='store_true',help='randomize a string')
parser.add_argument('-q', '--quiet', action='store_true',help='don\'t print the \'Output\' text')
args = parser.parse_args()


                    #if user doesn't pass any ints, this will be the default.
if not args.option1:
    if args.string: #default for '-s' option
        args.option1 = 100
    else:
        args.option1 = 1

if not args.option2:
    if args.string: #default for '-s' option
        args.option2 = 20
    else:
        args.option2 = 100


                    #prints 'Output:' unless user chose not to(with '-q')
if not args.quiet:
    print("Output:")

                    #prints a random number if user did not choose '-s'
if not args.string:
    if args.option1 <= args.option2:
        print(random.randrange(args.option1,args.option2 + 1))
    else:
        print(random.randrange(args.option2,args.option1 + 1))
else:
    if args.option1 < 0:      #'-s' --> -1=10000
        args.option1 = 10000
    if args.option1 < 33:       #'-s' --> add 33 to everything below 33
        args.option1 = args.option1 + 33
    for i in range(args.option2):
        print(chr(random.randrange(33,args.option1 + 1)), end="") #min is 33


    print("")
#created by https://github.com/000Daniel