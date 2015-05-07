#! /usr/bin/env Python
import glob
import os

def getFileNames():

    filenames = glob.glob("*")
    filenamesNoDir = []
    for filename in filenames:
        if os.path.isdir(filename):
            continue

        filenamesNoDir.append(filename)

    return filenamesNoDir

if __name__ == "__main__":
    filenames = getFileNames()
    print filenames
