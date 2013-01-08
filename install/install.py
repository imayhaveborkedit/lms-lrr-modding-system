import color
import wmi

def check():
    c = wmi.WMI()
    for cdrom in c.Win32_CDROMDrive():
        colors.color(" * CD Drives: ", color.FG_GREEN)
        vname = cdrom.VolumeName if cdrom.VolumeName is not None else "[None]"

        if u'OK' in cdrom.Status and cdrom.mediaLoaded:
            colors.color(u" - %s | " % cdrom.Drive, color.FG_GREEN, nl = False)
        else:
            colors.color(u" - %s | " % cdrom.Drive, color.FG_LIGHT_RED, nl = False)

        if "ROCKRAIDERS" in vname.upper():
            colors.color(vname, color.FG_GREEN)
        else:
            colors.color(vname, color.FG_LIGHT_RED)


def install(drive, location):

    pass