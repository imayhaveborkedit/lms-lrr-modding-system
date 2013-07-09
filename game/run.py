import subprocess
import bitdepth

# perhaps I should create a game object
# creating the object defines the enviroment
#

def launchLRR():
    print " Changing bit depth..."
    bitdepth.set_16()
    print " Launching game..."
    subprocess.call([r"LegoRR.exe"])
    print " Game terminated, restoring bit depth..."
    bitdepth.restore()
    print " Bit depth restored."


def overhaul(pack):
    #
    pass