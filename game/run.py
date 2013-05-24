import color, color.colors as colors
import subprocess
import bitdepth

def launchLRR():
    print " Changing bit depth..."
    bitdepth.set_16()
    print " Launching game..."
    subprocess.call([r"LegoRR.exe"])
    print " Game terminated, restoring bit depth..."
    bitdepth.restore()
    print " Bit depth restored."