#!/usr/bin/python3
import argparse

                    #these are the options that we can parse(pass) into this script.
parser = argparse.ArgumentParser(description="Convert text to binary and vice versa")
parser.add_argument('string', nargs='?' , type=str, help="passes a string into the script")
parser.add_argument('-t', '--totext', action='store_true',help='converts the string(binary code) to Text')
parser.add_argument('-b', '--tobinary', action='store_true',help='converts the string to Binary')
parser.add_argument('-s', '--includespace', action='store_true',help='converts the string with spaces between each character')
parser.add_argument('-q', '--quiet', action='store_true',help='doesn\'t print the \'Output\' text')
args = parser.parse_args()

                    #if user doesn't pass any string, this will be the default.
if not args.string:
    if not args.totext:
        args.string='Hmm'
    else:
        args.string='010010000110110101101101'
        
                    #'res' will be our final output(result).
res = ''

                    #if the user hasn't specified conversion to text, then convert to binary.
                    #conversion: convert each character in the string to binary code.
if not args.totext:
                    #if the user requested the result to be printed with spaces('-q').
    if args.includespace:
        res = ' '.join(format(ord(i), '08b') for i in args.string)
    else:
        res = ''.join(format(ord(i), '08b') for i in args.string)

                    #if the user has specified conversion to text('-t'), then convert binary code to text.
                    #conversion: takes 8 characters of 1's and 0's and converts them to bytes and then to characters.
                    #            then it erases 8 characters and sees if it can keep converting.
                    #            the script will output an error if the length of the code is below 8 1's and 0's
if args.totext:
                    #if the string contains any spaces:
    while ' ' in args.string:
                        #finds where is the first space.
        spaceIndex = args.string.index(' ')
                        #if the first space is the first letter, move the entire string one letter forward (' Hello' --> 'Hello').
        if spaceIndex == 0:
            args.string = args.string[1:]
        else:
                        #else, if first space is before the 9th character, print an error.
            if spaceIndex < 8:
                print('ERROR!, invalid binary code.')
                quit()
            else:
                res = res + chr(int(args.string[:8],2))
                args.string = args.string[8:]
                        #adds a space if user requested.
            if args.includespace:
                res = res + ' '
    else:
                    #if string doesn't contain ANY spaces.
        while len(args.string) > 0:
            res = res + chr(int(args.string[:8],2))
            args.string = args.string[8:]
                        #adds a space if user requested.
            if args.includespace:
                res = res + ' '

                    #if the user did not request for a quiet output, print 'Output:'
if not args.quiet:
    print("Output:")
print(res)