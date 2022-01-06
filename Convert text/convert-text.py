#!/usr/bin/python3
import argparse

                            #these lines get the launch options of this script
parser = argparse.ArgumentParser(description="created by https://github.com/000Daniel")
parser.add_argument('text', type=str, metavar='', nargs='?', help="pass a string into the script")
parser.add_argument('-u', '--uppercase', action='store_true', help="converts text's letters to uppercase")
parser.add_argument('-l', '--lowercase', action='store_true', help="converts text's letters to lowercase")
args = parser.parse_args()  #converts the flag data to something usable in script


if not args.text:           #if the user did not enter any text, this will be the default string
    args.text = "Default Text."

if args.uppercase:          #if the user used the '-u' flag but didn't the '-l'.
    if not args.lowercase:  #converts the text to upper-case.
        args.text = args.text.upper()  

if args.lowercase:          #if the user used the '-l' flag but didn't the '-u'.
    if not args.uppercase:  #converts the text to lower-case.
        args.text = args.text.lower()

print(args.text)
#created by https://github.com/000Daniel