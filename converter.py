#!/usr/bin/env python3
import os, sys

def pdfunite(args):
    userArguments = " "
    for arg in args:
        userArguments += (arg + " ") 
    os.system("pdfunite " + userArguments)

def main(args):
    opt = args[0]

    if opt == '-h':
        print ('--pdf -h')
        sys.exit()
    if opt == '--pdf':
        pdfunite(args[1:])
        sys.exit()    
        #test

if __name__ == "__main__":
   main(sys.argv[1:])