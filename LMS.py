import os
import sys
import subprocess

import colors
import OptionMenu

NAME = "LMS"
VERSION = "0.0.0"
SUBVERSION = " PRE ALPHA"
DEBUG = True

def preloadchecks():

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
    pass

################################################################################

def pc(t, c = 0x0):
    t = " * " + str(t)
    colors.pc(t,c)

def pd(i):
    if DEBUG: colors.pc(" @ " + str(i), colors.FOREGROUND_CYAN)

def p(i):
    print " * " + str(i)

################################################################################

def main():
    pc("Powering up LMS...", colors.FOREGROUND_GREEN)

    pc("Gathering environment varibles...", colors.FOREGROUND_GREEN)
    preloadobserve()

    pc("Running diagnostics...", colors.FOREGROUND_GREEN)
    preloadchecks()

    pc("System online.", colors.FOREGROUND_LIGHT_GREEN)

if __name__ == '__main__':
    print NAME + " Version " + VERSION + SUBVERSION + "\n"
    main()
