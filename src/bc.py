#!/usr/bin/env python3

import os
from shutil import which
import sys

# checks if the ImageMagick binaries are installed
def checkForImgMgk():
    return which("convert") is not None

def validateArgs():
    # firstly, has an argument been given?
    if(len(sys.argv) < 2):
        exit("Error: please provide an argument of the path to the images")
    elif(len(sys.argv) >= 3):
        exit("Error: please provide only 1 argument")

    # then, is the given argument a valid file path?
    if(not os.path.exists(sys.argv[1])):
        exit("Error: '" + sys.argv[1] + "' is not a valid file path")

    # if so, is the given argument pointing to a folder?
    if(not os.path.isdir(sys.argv[1])):
        exit("Error: '" + sys.argv[1] + "' is not a folder")

    # finally, does the folder contain only .jpg images?
    for file in os.listdir(sys.argv[1]):
        try:
            if(not file.split('.')[1].lower() == "jpg"):
                exit("Error: '" + file + "' is not a jpg file")
        except IndexError:
                exit("Error: '" + file + "' could not be parsed")

    # if program hasn't exited by this point, all is A-OK
    return True


def compress():
    wrapped = False
    for root, dirs, files in os.walk(os.path.abspath(sys.argv[1])):
        for file in files:
            baseFileName = file.split('.')[0] # remove file extension
            abs = os.path.join(root, file)
            # wrap absolute path in quotes if it contains any spaces
            if(' ' in abs):
                abs = "\"" + abs + "\""
                wrapped = True

            if(wrapped):
                command = "convert " + abs + " -quality 50% " + os.path.dirname(abs) + "/" + baseFileName + "-half.JPG\""
            else:
                command = "convert " + abs + " -quality 50% " + os.path.dirname(abs) + "/" + file + "-half.JPG"
            print("Compressing: " + file)
            os.system(command)

        print("Compression finished!")


if(__name__ == "__main__"):
    if(checkForImgMgk()):
        if(validateArgs()):
            compress()
    else:
        exit("Error: it doesn't seem that you have the ImageMagick binaries installed")
