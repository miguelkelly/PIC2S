#! /usr/bin/env python

import glob
import os
import sys

def getDirNames(path):
    formatedPath = '{0}{1}'.format(path,'*')
    dirnames = glob.glob(formatedPath)
    diramesNoFiles = []
    for dir in dirnames:
        if os.path.isfile(dir):
            continue

        dirnamesNoFiles.append(dir)
    return dirnamesNoFiles

if __name == "__main__":
    dirnames = getFileNames(sys.argv[1])
    print dirnames
