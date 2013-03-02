from color import colors

def launchLRR():
    # Figure out how to get/set color depth, hopefully without needing qres
    # Probably will need qres
    # I might not need to if Cyrem's tool works as expected.
    color.info("Launching game...")
    subprocess.call([r"LegoRR.exe"])
    color.info("Game terminated.")