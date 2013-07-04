import os
import sys
import time
import shutil
import textwrap
import zipfile
import bisect #wtf py2exe
import color
import color.colors as colors
from wad import wadtool
import game
from helper import term, menu

NAME = "LMS"
VERSION = "0.1.2"
SUBVERSION = "EXTREME TEST EDITION"
DEBUG = True
LMSREADY = False
WADSAREPRIME = False

## GUI STUFF ###################################################################

def initGUI():
    pd("GUI disabled (nonexistant).")
    # program should probably terminate if this fails to loads properly.

## INITALIATION STUFF ##########################################################

def initLMS():

    #check for update

    global LMSREADY
    LMSREADY = True
    preloadobserve()
    preloadchecks()
    if LMSREADY:
        colors.pc("System online, initalizing interface (but not really)...", color.FG_LIGHT_GREEN)
        initGUI()


def preloadobserve():
    colors.pc("Gathering environment varibles...", color.FG_GREEN)
    if 'Program Files' in os.getcwd():
        colors.pc("Warning: Running from Program Files folder.  Not advised.  [insert stuff/menu here]", color.FG_LIGHT_YELLOW)
    #import install
    #install.check()


def preloadchecks():
    colors.pc("Running preload checks...", color.FG_GREEN)

    pd(os.getcwd())
    if DEBUG:
        pd("Cheating, moving to")
        os.chdir(r"C:/Users/Daniel/Desktop/lrr-notprime") # TEMPORARY HACK
        pd(os.getcwd())

    try:
        with open('LegoRR.exe') as f:
            pd("Executable located.")
            global WADSAREPRIME
            WADSAREPRIME = wadtool.checkwads()
            if os.path.exists("d3drm.dll"):
                if hasattr(sys,"frozen") and sys.frozen in ("windows_exe", "console_exe"):
                    zipf = zipfile.ZipFile(sys.executable)
                    zipf.extract("d3drm.dll")
    except BaseException, e:
        global LMSREADY
        LMSREADY = False
        if not r"C:/Program Files" in os.getcwd():
            print ""
            tex = textwrap.wrap("Game not found.  I'm going to go now. "+
            "I suggest you put this in the same folder as the Rock Raiders exe, like you were told to do.\n")
            # add search function?
            for t in tex: print " " + t
            cleanup()
        else:
            tex = textwrap.wrap(
            "You've got the game installed, but you shouldn't mess with the copy in Program"+
            "Files.  Usually you copy it elsewhere for modding, so you have a clean copy"+
            "for when it inevitably breaks.  Your Desktop is usually a good place for it.\n"+
            "Want me to do that for you?\n")
            for t in tex: print " " + t

            print "[YES/no] ",
            sys.stdout.flush()
            try: r = str(sys.stdin.readline()[:-1])
            except: r = None
            if 'yes' in r.lower() or r is None:
                # add testing for files
                shutil.copytree(os.getcwd(), os.path.join(os.path.expanduser('~/Desktop/'), os.path.basename(os.getcwd())))
        #return


## SHUTDOWN STUFF ##############################################################

def cleanup():
    colors.color(" * Powering down...", color.FG_GREEN)
    # cleanup curses
    # curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()
    sys.exit()

## blar ########################################################################

def pd(i):
    if DEBUG: colors.color(" @ " + str(i), color.FG_CYAN)

## MAIN MENU, WILL BE REPLACED BY GUI ## PROBABLY ## MAYBE #####################

def mainmenu():
    global WADSAREPRIME
    while True:
        print
        print " Game: ",
        if LMSREADY:
            colors.color("Ready", color.FG_LIGHT_GREEN)
            print " WADs: ",
            if WADSAREPRIME:
                colors.color("Primed for Data Method", color.FG_LIGHT_GREEN)
            else:
                colors.color("Not primed", color.FG_LIGHT_YELLOW)

        else: colors.color("Not ready", color.FG_LIGHT_RED)
        print

        menu_main = menu.Menu([("Launch LRR", launchGame),("Prime WADs", primeWADs),("Quit", cleanup)])
        menu_main.indent = 1
        menu_main.prompt = ">"
        selectedopt = menu_main.open()
        selectedopt()

        cls()

def launchGame():
    game.run.launchLRR() # add option for Cafeteria

def primeWADs():
    if not wadtool.checkwads(): WADSAREPRIME = wadtool.primewads()
    else: colors.color("Wad check failed.", color.FG_YELLOW)

################################################################################

def cls():
    os.system('cls')

def main():
    colors.pc("Powering up LMS...", color.FG_GREEN)
    try:
        initLMS()
        mainmenu()
    except SystemExit: return
    except BaseException as e:
        print "Something bad has happened, due most likely to my ineptitude."
        print "This is what happened.  Paste this in the LMS topic or somehow tell Doc.\n"
        print '*' * term.getX()
        print
        print e
        print
        print '*' * term.getX()
        print

    cleanup()

if __name__ == '__main__':
    print NAME + " Version " + VERSION + ' ' + SUBVERSION + "\n"
    main()
