import sys
import wmi
import subprocess
import zipfile
import color
import color.colors as colors

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
    else:
        print "something something ask user"


def install(drive, location=None):
    if hasattr(sys,"frozen") and sys.frozen in ("windows_exe", "console_exe"):
        extractresources()



def extractresources():
    zipf = zipfile.ZipFile(sys.executable)
    res = ["d3drm.dll", "i5comp.exe","ZD51145.DLL"]
    [zipf.extract(r) for r in res]