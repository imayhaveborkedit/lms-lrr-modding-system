import os
import sys
import subprocess
import colors

NAME = "LMS"
VERSION = "0.0.0"
SUBVERSION = " PRE ALPHA"
DEBUG = True

def preloadchecks():

    pd(os.getcwd())
    os.chdir(r"C:/Users/Daniel/Desktop/lrr")
    pd(os.getcwd())

    try:
        with open('LegoRR.exe') as f:
            pd("Executable located.")
            pass
    except BaseException as e:
        p("Game not found.  Aborting.")


def launchLRR():
    p("Launching game...")
    subprocess.call([r"LegoRR.exe"])
    p("Game terminated.")

def preloadobserve():
    pass

def pd(i):
    if DEBUG: print " @ " + str(i)

def p(i):
    print " - " + str(i)

def main():
    p("Powering up LMS...")

    pd("Gathering environment varibles...")
    preloadobserve()

    pd("Running diagnostics...")
    preloadchecks()

    colors.pc("System online.", colors.FOREGROUND_GREEN)

if __name__ == '__main__':
    print NAME + " Version " + VERSION + SUBVERSION + "\n"
    main()
