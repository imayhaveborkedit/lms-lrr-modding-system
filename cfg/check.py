import sys
import os
import re
import time
from .. import colors

f = os.path.join("C:/Users/Daniel/Desktop/lrr","Data/Lego.cfg")
def check():
    line = "a"
    regex = re.compile("^[^\s;}]\w?\s*[^};]*") #BLARG
    with open(f) as cfg:
        while line is not None:
            line = cfg.readlines()
            print line
            return
            line = cfg.readline().strip()

            result = regex.match(line)
            if result:
                colors.pc(result.group(0), colors.FOREGROUND_GREEN)
                #get folders in Data folder, match file locations, check if exists

            else:
                colors.pc("NO:  " + line, colors.FOREGROUND_RED)
    os.chdir(r"C:\Users\Daniel\Desktop\lrr") # TEMPORARY HACK
    print os.listdir("Data")
