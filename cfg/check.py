import sys
import os
import re
import time
import glob
from color import colors

f = os.path.join("C:/Users/Daniel/Desktop/lrr-prime","Data/Lego.cfg") # TEMPORARY HACK

linenumber = 0
rootfolders = tuple(os.listdir("Data"))
pathregex = re.compile('([a-zA-Z0-9_]/)*\.(bmp|txt|npl|ol|ptl|map|avi|flh)', re.IGNORECASE)
rgbregex = re.compile('\d{1,3}:\d{1,3}:\d{1,3}')
rgbrange = range(256)
isfile = os.path.isfile

def check():
    global linenumber
    regex = re.compile("^[^\s;}{]\w*\s*[^}{;/]+") # works almost perfectly
    with open(f) as cfg: #change once implemented
        lines = cfg.readlines()
        for line in lines:
            linenumber+=1
            result = regex.match(line.strip())
            if result:
                vset = result.group(0).split()
                if len(vset) == 2:
                    dochecks(vset)
                """
                colors.color(result.group(0), color.FG_LIGHT_GREEN)
                colors.color(vset, color.FG_GREEN)

            else:#pass
                colors.color(line.strip(), color.FG_RED)
                lines.remove(line)"""


def dochecks(line):
    confirmpath(line)
    rgbcheck(line)
    # other checks...

def confirmpath(line):
    # this should work when frozen and in the right dir though (main will not use higher functions when not in an LRR dir)
    #rootfolders = os.listdir("Data")

    l = line[1]
    joinpath = os.path.join("Data", l)

    if l.startswith(rootfolders): # obvious first check
        if ',' in l: # put this aside for further testing
            if os.path.isfile(joinpath[:joinpath.index(',')]): # tweak path
                #colors.color(joinpath[:joinpath.index(',')], color.FG_LIGHT_GREEN, nl = False)
                #colors.color('\b' + joinpath[joinpath.index(','):], color.FG_LIGHT_GREEN | color.BG_RED)
                pass

            else: pass #colors.color(joinpath, color.FG_LIGHT_RED)

        #elif '::' in l: # nothing to bother with these
        #    print l

        elif ':' in l and not '::' in l: #pass
            print l
            print

        elif '|' in l: #pass # i'm getting really tired of your crap, cfg
            stuff = l.split('|')
            stuff = stuff[:-2]
            # blar check length, if more than 1, do stuff
            if islrrpath(stuff[0]):pass

        elif '.' in l:
            if not os.path.isfile(joinpath): pass
                #displaywarning(line[0]+' -> '+l, "File does not exist. (No %s)" % line[0])

        else: # if we have one of those no-extension paths
            if os.path.isdir(joinpath):
                gl = glob.glob(joinpath + '\\*.*')
                if len(gl)==0:
                    displaypossibleerror(line[0]+'  '+l, "Missing resources?")
            #else: pass # Ignore because the game seems to be fine without them

def rgbcheck(line):
    if "RGB" in line[0] and not line[0].endswith(('Min', 'Max')):
        rgbparts = line[1].split(':')
        for rgbpart in rgbparts:
            if int(rgbpart) not in rgbrange:
                displayerror(line[0]+'  '+line[1], "Invalid RGB value.")

def islrrpath(string): # good enough for now
    return string.startswith(rootfolders)

def displaywarning(item, message):
    colors.color("[Warning] On line %i, %s: \n%s\n" % (linenumber, item, message), color.FG_LIGHT_YELLOW)

def displaypossibleerror(item, message):
    colors.color("[Possible Error] On line %i, %s: \n%s\n" % (linenumber, item, message), color.FG_RED)

def displayerror(item, message):
    colors.color("[Error] On line %i, %s: \n%s\n" % (linenumber, item, message), color.FG_LIGHT_RED)









