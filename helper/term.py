from ctypes import windll, create_string_buffer
import struct


def getX():
    return getTerminalSize()[0]


def getY():
    return getTerminalSize()[1]


def getTerminalSize():
    res = None
    try:
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    except:
        return [None, None]
    if res:
        (bufx, bufy, curx, cury, wattr,
         left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
        return sizex, sizey
    else:
        return [None, None]