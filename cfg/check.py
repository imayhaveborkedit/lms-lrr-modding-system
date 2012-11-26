import sys
import os
import re
import time

#os.chdir(r"C:/Users/Daniel/Desktop/lrr") # TEMPORARY HACK
f = os.path.join("C:/Users/Daniel/Desktop/lrr","Data/Lego.cfg")
def check():
    line = ""
    regex = re.compile("^[^\s;}]\w?\s*[^};]*") #BLARG
    with open(f) as cfg:
        while line is not None:
            line = cfg.readline().strip()
            result = regex.match(line)
            if result:
                print len(result.group(0))
                #get folders in Data folder, match file locations, check if exists
            else:
                print "NO:  " + line
