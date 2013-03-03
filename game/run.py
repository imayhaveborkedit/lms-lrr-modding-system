import color, color.colors as colors
import subprocess

def launchLRR():
    # Figure out how to get/set color depth, hopefully without needing qres
    # Probably will need qres
    # I might not need to if Cyrem's tool works as expected.
    print " Launching game..."
    subprocess.call([r"LegoRR.exe"])
    print " Game terminated."