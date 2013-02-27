import color
import wmi
import subprocess

def check():
    c = wmi.WMI()
    drive = None
    for cdrom in c.Win32_CDROMDrive():
        colors.color(" * CD Drives: ", color.FG_GREEN)
        vname = cdrom.VolumeName if cdrom.VolumeName is not None else "[None]"

        if u'OK' in cdrom.Status and cdrom.mediaLoaded:
            colors.color(u" - %s | " % cdrom.Drive, color.FG_GREEN, nl = False)
        else:
            colors.color(u" - %s | " % cdrom.Drive, color.FG_LIGHT_RED, nl = False)

        names = ["ROCKRAIDERS", "ROCK RAIDERS"]
        if vname.upper() in names:
            colors.color(vname, color.FG_GREEN)
            drive = cdrom.Drive
        else:
            colors.color(vname, color.FG_LIGHT_RED)


    if drive is not None:
        install(drive)
    else: pass # prompt for stuff if needed


def install(drive, location=None):
    # Extract resources
    pass