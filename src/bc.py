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
        exit("""Error: please provide, at minimum, an argument of the path to the images.
        -> $ bc.py <path> <(default 50) compression percentage>""")
    elif(len(sys.argv) >= 4):
        exit("""Error: please provide no more than 2 arguments.
        -> $ bc.py <path> <(default 50) compression percentage>""")

    if(len(sys.argv) == 3):
        try:
            sys.argv[2] = int(sys.argv[2])
            # if not caught, arg 2 is an int
        except  ValueError:
            exit("""Second argument must be an int.
                -> $ bc.py <path> <(default 50%) compression percentage>""")

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
    # return true with a compression percentage. Hardcoded 50% if not
    # decided by the user
    if(len(sys.argv) == 3):
        return True, sys.argv[2]
    else:
        return True, 50


def compress(compressionPercent):
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
                command = "convert " + abs + " -quality " + str(compressionPercent) + "% " + os.path.dirname(abs) + "/" + baseFileName + "-compressed.JPG\""
                print(command)
            else:
                command = "convert " + abs + " -quality " + str(compressionPercent) + "% " + os.path.dirname(abs) + "/" + file + "-compressed.JPG"
                print(command)
            print("Compressing: " + file)
            os.system(command)

        print("Compression finished!")


if(__name__ == "__main__"):
    if(checkForImgMgk()):
        validated, compressionPercent = validateArgs()
        if(validated):
            compress(compressionPercent)

    else:
        exit("Error: it doesn't seem that you have the ImageMagick binaries installed")
