#!/usr/bin/env python3
# Robert Sturzbecher 2022-04-19 
# MD5 file checksum calculator for assessment project

import sys
# import argparse  # for more advanced args, maybe later add 
import hashlib
from functools import partial

class colors:                                           # ANSI terminal color escape codes, excuse my american spelling here but that is how the ANSI standard spells it ;)
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END = '\033[0m'
    

def getmd5(filename):                                   # calculates the MD5 checksum of the file specified 
    try:
        with open(filename, mode='rb') as file:         # rb = Read, binary mode 
            hash = hashlib.md5()
            for buffer in iter(partial(file.read, 1024), b''):   # increased buffer from 128 to 1024, try 4096 for faster processing   
                hash.update(buffer)
        return hash.hexdigest()                         # Test and compare under windows with "certutil -hashfile filename MD5" to make sure matches
    except OSError:                                     # error opening file, may not exist or can not access for some other reason
        print(f"{colors.RED}Error opening file{colors.END}")
        sys.exit()     

def printHelp():
    print("Usage: MD5 [filename]\n")
    return


def main():
    print(f"{colors.GREEN}File MD5 checksum calculator [Robert Sturzbecher]{colors.END}") 
    if len(sys.argv) != 2 :                             # correct usage would return 2, this scrip full filename and the filename of the file to calc MD5 for
        print(f"{colors.RED}Error: Filename argument missing{colors.END}")
        printHelp()
    elif str(sys.argv) == "-h":                         # Print help screen help 
        printHelp()                 
    else :
        filename=sys.argv[-1]                           # gets the last argument, if non given it will return this script filename 
        print(f"{colors.YELLOW}File: {filename}{colors.END}")
        print(f"{colors.YELLOW}MD5: {getmd5(filename)}{colors.END}")


if __name__ == "__main__":    
    main()                              