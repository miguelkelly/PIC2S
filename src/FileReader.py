#! /usr/bin/env Python
import glob
import os
import sys

def getFileNames(path):

    formatedPath = '{0}{1}'.format(path,'*')
    filenames = glob.glob(formatedPath)
    filenamesNoDir = []
    for filename in filenames:
        if os.path.isdir(filename):
            continue

        filenamesNoDir.append(filename)

    return filenamesNoDir

if __name__ == "__main__":
    filenames = getFileNames(sys.argv[1])
    print sys.argv[1]
    print filenames
