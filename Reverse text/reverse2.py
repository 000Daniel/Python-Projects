#!/usr/bin/python3
import argparse

                            #these lines get the launch options of this script
parser = argparse.ArgumentParser(description="created by https://github.com/000Daniel")
parser.add_argument('text', type=str, metavar='', nargs='?', help="pass a string into the script")
parser.add_argument('-q', '--quiet', action='store_true', help="removes the \'Output\' text")
args = parser.parse_args()  #converts the flag data to something usable in script


if not args.text:           #if the user did not enter any text, this will be the default string
    args.text = "]-: ytpme"

reversedText = ""                       #reverses the text
for ch in args.text:                    #for each character('ch') in the user's text:
    reversedText = ch + reversedText    #add that character to the beginning of the output('reversedText')

if not args.quiet:          #prints 'Output:' if quiet flag is not applied
    print ("Output:")
print (reversedText)        #prints reversed text
#created by https://github.com/000Daniel