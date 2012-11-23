import sys
import ctypes

FOREGROUND_BLACK         = 0x00
FOREGROUND_BLUE          = 0x01
FOREGROUND_GREEN         = 0x02
FOREGROUND_CYAN          = 0x03
FOREGROUND_RED           = 0x04
FOREGROUND_MAGENTA       = 0x05
FOREGROUND_YELLOW        = 0x06
FOREGROUND_LIGHT_GREY    = 0x07

FOREGROUND_DARK_GREY     = 0x08
FOREGROUND_LIGHT_BLUE    = 0x09
FOREGROUND_LIGHT_GREEN   = 0x0A
FOREGROUND_LIGHT_CYAN    = 0x0B
FOREGROUND_LIGHT_RED     = 0x0C
FOREGROUND_LIGHT_MAGENTA = 0x0D
FOREGROUND_LIGHT_YELLOW  = 0x0E
FOREGROUND_WHITE         = 0x0F


BACKGROUND_BLACK         = 0x00
BACKGROUND_BLUE          = 0x10
BACKGROUND_GREEN         = 0x20
BACKGROUND_CYAN          = 0x30
BACKGROUND_RED           = 0x40
BACKGROUND_MAGENTA       = 0x50
BACKGROUND_YELLOW        = 0x60
BACKGROUND_LIGHT_GREY    = 0x70
BACKGROUND_DARK_GREY     = 0x80

BACKGROUND_LIGHT_BLUE    = 0x90
BACKGROUND_LIGHT_GREEN   = 0xA0
BACKGROUND_LIGHT_CYAN    = 0xB0
BACKGROUND_LIGHT_RED     = 0xC0
BACKGROUND_LIGHT_MAGENTA = 0xD0
BACKGROUND_LIGHT_YELLOW  = 0xE0
BACKGROUND_WHITE         = 0xF0


STD_OUTPUT_HANDLE = -11

def get_csbi_attributes(handle):
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr

def pc(text, color):
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    print text,
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    print ""
    sys.stdout.flush()

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)