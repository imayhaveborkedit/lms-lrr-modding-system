import os
import sys
import subprocess
import time
import shutil
import game
import color
import color.colors as colors
from wad import wadtool

NAME = "LMS"
VERSION = "0.0.0"
SUBVERSION = "SUPER DUPER NOT READY YET"
DEBUG = True
LMSREADY = False
WADSAREPRIME = False

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
    #import install.install
    #install.install.check()
    # lolololol ^

def preloadchecks():
    colors.pc("Running preload checks...", color.FG_GREEN)

    pd(os.getcwd())
    pd("Cheating, moving to")
    if DEBUG: os.chdir(r"C:/Users/Daniel/Desktop/lrr-notprime") # TEMPORARY HACK
    pd(os.getcwd())

    try:
        with open('LegoRR.exe') as f:
            pd("Executable located.")
    except BaseException, e:
        if not r"C:/Program Files" in os.getcwd():
            colors.pc("""Game not found.  I'm going to go now.  When there's a game then I can help you.
            I suggest you put this in the same folder as the exe, like you were told to do.""")
        else:
            colors.pc("""You've got the game installed, but you shouldn't mess with the copy in Program
            Files.  Usually you copy it elsewhere for modding, so you have a clean copy
            for when it inevitably breaks.  Your Desktop is usually a good place for it.

            Want me to do that for you?\n""", color.FG_LIGHT_YELLOW)
            print "[YES/no] ",
            sys.stdout.flush()
            try: r = str(sys.stdin.readline()[:-1])
            except: r = None
            if 'yes' in r.lower() or r is None:
                # add testing for files
                shutil.copytree(os.getcwd(), os.path.join(os.path.expanduser('~/Desktop/'), os.path.basename(os.getcwd())))
    global WADSAREPRIME
    WADSAREPRIME = wadtool.checkwads()


## SHUTDOWN STUFF ##############################################################

def cleanup():
    colors.color(" * Powering down...", color.FG_GREEN)

## blar ########################################################################

def pd(i):
    if DEBUG: colors.color(" @ " + str(i), color.FG_CYAN)

## MAIN MENU, WILL BE REPLACED BY GUI ##########################################

def mainmenu():
    global WADSAREPRIME
    while True:
        print;
        o = []

        print " Game: ",
        if LMSREADY: colors.color("Ready", color.FG_LIGHT_GREEN); o += ["Launch LRR"]
        else: colors.color("Not ready", color.FG_LIGHT_RED)

        print " WADs: ",
        if WADSAREPRIME: colors.color("Primed for Data Method", color.FG_LIGHT_GREEN)
        else: colors.color("Not primed.", color.FG_LIGHT_YELLOW); o += ["Prime WADs"]

        print;
        o += ["Quit"]

        for opt in range(len(o)):
            print " [%d] %s" % (opt+1, o[opt])

        print "\n >",
        sys.stdout.flush()
        try: r = int(sys.stdin.readline()[:-1])
        except: r = None
        print;

        try:
            selected = o[r-1]
        except: selected = 0

        if not selected:
            print "Wut?"
        else:
            if selected == "Launch LRR": game.run.launchLRR()
            elif selected == "Prime WADs":
                if not wadtool.checkwads(): WADSAREPRIME = wadtool.primewads()
                else: colors.color("Wad check failed.", color.FG_YELLOW)
            elif selected == "Quit" or r is None: break

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
