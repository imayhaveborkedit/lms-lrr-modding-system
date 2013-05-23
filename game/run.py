import color, color.colors as colors
import subprocess
import bitdepth

def launchLRR():
    print " Changing bitdepth..."
    bitdepth.set_16()
    print " Launching game..."
    subprocess.call([r"LegoRR.exe"])
    print " Game terminated, restoring bitdepth..."
    bitdepth.restore()
    print " Bitdepth restored."