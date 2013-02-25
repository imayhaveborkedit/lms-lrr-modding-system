import os
import sys
import subprocess
import time
import shutil
import color
import color.colors as colors
from wad import wadtool

NAME = "LMS"
VERSION = "0.0.0"
SUBVERSION = "SUPER DUPER NOT READY YET"
DEBUG = True
LMSREADY = False

## GUI STUFF ###################################################################

def initGUI():
    pd("GUI disabled (nonexistant).")

## INITALIATION STUFF ##########################################################

def initLMS():
    preloadobserve()
    preloadchecks()

    colors.pc("System online, initalizing interface (but not really)...", color.FG_LIGHT_GREEN)
    initGUI()
    global LMSREADY
    LMSREADY = True

def preloadobserve():
    colors.pc("Gathering environment varibles...", color.FG_GREEN)
    if 'Program Files' in os.getcwd():
        colors.pc("Warning: Running from Program Files folder.  Not advised.  [insert stuff/menu here]", color.FG_LIGHT_YELLOW)
    import install

def preloadchecks():
    colors.pc("Running preload checks...", color.FG_GREEN)
    pd(os.getcwd())
    pd("Cheating, moving to")
    os.chdir(r"C:/Users/Daniel/Desktop/lrr-notprime") # TEMPORARY HACK
    pd(os.getcwd())

    wadtool.checkwads()

    try:
        with open('LegoRR.exe') as f:
            pd("Executable located.")
    except BaseException, e:
        if not checkProgramFilesInstall():
            colors.pc("""Game not found.  I'm going to go now.  When there's a game then I can help you.
            I suggest you put this in the same folder as the exe, like you were told to do.""")
        else:
            colors.pc("""You've got the game installed, but you shouldn't mess with the copy in Program
            Files.  Usually you copy it else where for modding, so you have a clean copy
            for when it inevitably breaks.  Your Desktop is usually a good place for it.

            Want me to do that for you?\n""", color.FG_LIGHT_YELLOW)
            print "[YES/no] ",
            sys.stdout.flush()
            try: r = str(sys.stdin.readline()[:-1])
            except: r = None
            if 'yes' in r.lower() or r is None:
                # add testing for files
                shutil.copytree(os.getcwd(), os.path.join(os.path.expanduser('~/Desktop/'), os.path.basename(os.getcwd())))



def checkProgramFilesInstall():
    return r"C:/Program Files" in os.getcwd()


def launchLRR():
    # Figure out how to get/set color depth, hopefully without needing qres
    # Probably will need qres
    color.info("Launching game...")
    subprocess.call([r"LegoRR.exe"])
    color.info("Game terminated.")


## SHUTDOWN STUFF ##############################################################

def cleanup():
    colors.color("\n * Powering down...", color.FG_GREEN)

## blar ########################################################################

def pd(i):
    if DEBUG: colors.color(" @ " + str(i), color.FG_CYAN)

## MAIN MENU, WILL BE REPLACED BY GUI ##########################################

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
