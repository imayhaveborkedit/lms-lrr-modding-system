import sys
import os
import re
import time
import glob
sys.path.append(os.path.normpath(os.path.join(sys.path[0],'..')))
import color.colors as colors

f = os.path.join("C:/Users/Daniel/Desktop/lrr","Data/Lego.cfg") # TEMPORARY HACK
linenumber = 0
pathregex = re.compile('([a-zA-Z0-9_]/)*\.(bmp|txt|npl|ol|ptl|map|avi|flh)')

def check():
    linenumber = 0
    regex = re.compile("^[^\s;}{]\w*\s*[^}{;/]+") # works almost perfectly
    with open(f) as cfg:
        lines = cfg.readlines()
        linenumber+=1
        for line in lines:
            result = regex.match(line.strip())
            if result:
                vset = result.group(0).split()
                if len(vset) == 2:
                    dochecks(vset)
                #colors.pc(result.group(0), colors.FOREGROUND_LIGHT_GREEN)
                #colors.pc(vset, colors.FOREGROUND_GREEN)

            #else:pass
                #colors.pc(line.strip(), colors.FOREGROUND_RED)
                #lines.remove(line)


def dochecks(line):
    confirmpath(line)

def confirmpath(line):

    # TEMPORARY HACK
    os.chdir(r"C:\Users\Daniel\Desktop\lrr")

    # this should work when frozen and in the right dir though (main will not use higher functions when not in an LRR dir)
    rootfolders = os.listdir("Data")

    l = line[1]
    joinpath = os.path.join("Data", l)

    if l.startswith(tuple(rootfolders)): # obvious first check
        if ',' in l: # put this aside for further testing
            if os.path.isfile(joinpath[:joinpath.index(',')]): # tweak path
                #colors.pc(joinpath[:joinpath.index(',')], colors.FOREGROUND_LIGHT_GREEN, nl = False)
                #colors.pc('\b' + joinpath[joinpath.index(','):], colors.FOREGROUND_LIGHT_GREEN | colors.BACKGROUND_RED)
                pass

            else: pass #colors.pc(joinpath, colors.FOREGROUND_LIGHT_RED)

        elif '.' in l:
            if os.path.isfile(joinpath): # file exists, should be complete match
                pass #colors.pc(joinpath, colors.FOREGROUND_LIGHT_GREEN)

            else: pass #colors.pc(joinpath, colors.FOREGROUND_LIGHT_RED)

        elif '::' in l: pass # more tweaking

        elif ':' in l: pass # weeeeeee...

        else: # if we have one of those no-extension paths
            if os.path.isdir(joinpath):
                colors.pc(l, colors.FOREGROUND_LIGHT_YELLOW)
                gl = glob.glob(joinpath + '\\*.*')
                if len(gl)==0:

                    print line[0] + " -> " + line[1]
                    print gl
            else: pass # Ignore because the game seems to be fine without them


def displaywarning(item, message):
    colors.pc("[Warning] %s: %s" % (item, message), colors.FOREGROUND_LIGHT_YELLOW)

def displaypossibleerror(item, message):
    colors.pc("[Possible Error] %s: %s" % (item, message), colors.FOREGROUND_RED)

def displayerror(item, message):
    colors.pc("[Error] %s: %s" % (item, message), colors.FOREGROUND_LIGHT_RED)














