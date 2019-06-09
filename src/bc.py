#!/usr/bin/env python3

from os import system, path, listdir
import sys

def validateArgs():
    # firstly, has an argument been given?
    if(len(sys.argv) < 2):
        exit("Error: please provide an argument of the path to the images")

    # then, is the given argument a valid file path?
    if(not path.exists(sys.argv[1])):
        exit("Error: '" + sys.argv[1] + "' is not a valid file path")

    # if so, is the given argument pointing to a folder?
    if(not path.isdir(sys.argv[1])):
        exit("Error: '" + sys.argv[1] + "' is not a folder")

    # finally, does the folder contain only images?
    for file in listdir(sys.argv[1]):
        if(not file.split('.')[1].lower() == "jpg"):
            exit("Error: '" + file + "' is not a jpg file")

    # if program hasn't exited by this point, all is A-OK
    return True



if(__name__ == "__main__"):
    if(validateArgs()):
        print("Passed")
    else:
        print("Failed")
