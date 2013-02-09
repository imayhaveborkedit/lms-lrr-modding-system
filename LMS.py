import os
import sys
import subprocess
import time
import color
import color.colors as colors
from wad import wadtool

NAME = "LMS"
VERSION = "0.0.0"
SUBVERSION = "SUPER DUPER NOT READY YET"
DEBUG = True
LMSREADY = False


################################################################################

def initGUI():
    pd("GUI disabled (nonexistant).")

################################################################################

def initLMS():
    preloadobserve()
    preloadchecks()

    colors.pc("System online, initalizing interface (but not really)...", color.FG_LIGHT_GREEN)
    initGUI()
    global LMSREADY
    LMSREADY = True

def preloadchecks():
    colors.pc("Running preload checks...", color.FG_GREEN)
    pd(os.getcwd())
    os.chdir(r"C:/Users/Daniel/Desktop/lrr-notprime") # TEMPORARY HACK
    pd(os.getcwd())

    wadtool.checkwads()

    try:
        with open('LegoRR.exe') as f:
            pd("Executable located.")
    except BaseException, e:
        colors.pc("Game not found.  Aborting.")


def launchLRR():
    # Figure out how to get/set color depth, hopefully without needing qres
    color.info("Launching game...")
    subprocess.call([r"LegoRR.exe"])
    color.info("Game terminated.")

def preloadobserve():
    colors.pc("Gathering environment varibles...", color.FG_GREEN)
    if 'Program Files' in os.getcwd():
        colors.pc("Warning: Running from Program Files folder.  Not advised.  [insert stuff/menu here]", color.FG_LIGHT_YELLOW)
    import install

################################################################################

def cleanup():
    colors.color("\n * Powering down...", color.FG_GREEN)

################################################################################

def pd(i):
    if DEBUG: colors.color(" @ " + str(i), color.FG_CYAN)

################################################################################

def mainmenu():
    while True:
        print;
        o = ["[1] Launch game","[2] Prime WADs","[3] Quit"]

        [colors.color(" "+oo, color.FG_WHITE) for oo in o]

        print "\n >",
        sys.stdout.flush()
        try: r = int(sys.stdin.readline()[:-1])
        except: r = None

        if r == 1: launchLRR()
        elif r == 2:
            if wadtool.checkwads(): wadtool.primewads()
        elif r == 3 or None: break

################################################################################

def main():
    colors.pc("Powering up LMS...", color.FG_GREEN)
    initLMS()
    mainmenu()
    cleanup()
    print "\n Good bye"

if __name__ == '__main__':
    print NAME + " Version " + VERSION + ' ' + SUBVERSION + "\n"
    main()
