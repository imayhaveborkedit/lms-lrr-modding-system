import os
import sys
import subprocess
import time
import color.colors as colors

NAME = "LMS"
VERSION = "0.0.0"
SUBVERSION = " PRE ALPHA"
DEBUG = True

LMSREADY = False



################################################################################

def initGUI():
    pd("GUI disabled temporarily.")

################################################################################

def initLMS():
    preloadobserve()
    preloadchecks()

    pc("System online, initalizing interface...", colors.FOREGROUND_LIGHT_GREEN)
    initGUI()
    global LMSREADY
    LMSREADY = True

def preloadchecks():
    pc("Running diagnostics...", colors.FOREGROUND_GREEN)

    pd(os.getcwd())
    os.chdir(r"C:/Users/Daniel/Desktop/lrr") # TEMPORARY HACK
    pd(os.getcwd())

    try:
        with open('LegoRR.exe') as f:
            pd("Executable located.")
            pass
    except BaseException as e:
        pc("Game not found.  Aborting.", )


def launchLRR():
    p("Launching game...")
    subprocess.call([r"LegoRR.exe"])
    p("Game terminated.")

def preloadobserve():
    pc("Gathering environment varibles...", colors.FOREGROUND_GREEN)

################################################################################

def cleanup():
    colors.pc("\n * Powering down...", colors.FOREGROUND_GREEN)

################################################################################

def pc(t, c = 0xf, nl = True):
    t = " * " + str(t)
    colors.pc(t,c, nl)

def pd(i):
    if DEBUG: colors.pc(" @ " + str(i), colors.FOREGROUND_CYAN)

def p(i):
    print " * " + str(i)

################################################################################

def mainmenu():
    while True:
        print;
        o = ["[1] Launch game","[2] Quit"]

        [colors.pc(" "+oo, colors.FOREGROUND_WHITE) for oo in o]

        print "\n >",
        sys.stdout.flush()
        try: r = int(sys.stdin.readline()[:-1])
        except: r = None

        if r == 1: launchLRR()
        elif r == 2 or None: break

################################################################################

def main():
    pc("Powering up LMS...", colors.FOREGROUND_GREEN)
    initLMS()
    mainmenu()
    cleanup()
    print "\n Good bye"

if __name__ == '__main__':
    print NAME + " Version " + VERSION + SUBVERSION + "\n"
    main()
