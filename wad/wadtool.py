#! /usr/bin/python

#Copyright (C) 2009 Johan Grip
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import os
import shutil
import glob
import wad

def usage():
    print """
Usage:
    e <wadfile> <destination>
       Unpacks wadfile into destination directory.
    p <wadfile> <source>
       Creates a new wadfile from a source directory.
"""

def main():
    print "WAD Tool 0.1"
    if len(sys.argv) != 4:
        usage()
        exit()

    if sys.argv[1] == 'e':
        print "Reading wad file %s" % (sys.argv[2])
        try:
            wadfile = wad.load(sys.argv[2])
        except IOError, err:
            print err
            exit()
        print "Extracting into %s" % (sys.argv[3])
        try:
            wadfile.extract(sys.argv[3])
        except IOError, err:
            print err

    if sys.argv[1] == 'p':
        print "Reading directory %s" % (sys.argv[3])
        try:
            wadfile = wad.fromdirectory(sys.argv[3])
        except IOError, err:
            print err
            exit()
        print "Saving WAD file %s" % (sys.argv[2])
        try:
            wadfile.save(sys.argv[2])
        except IOError, err:
            print err

if __name__ == "__main__":
    main()

# End ogun code ################################################################

def extract(wadfile, outfolder=None):
    if outfolder is None:
        outfolder = os.path.normpath(os.path.join(os.path.dirname(wadfile), os.path.basename(wadfile)[:os.path.basename(wadfile).index('.')]))
    print "Reading wad file %s" % (wadfile)
    olddir = os.getcwd()
    os.chdir(os.path.dirname(wadfile))
    try:
        print outfolder
        os.makedirs(outfolder)
    except: pass # folder already created or something
    try:
        wadfile = wad.load(wadfile)
    except IOError, err:
        print err
        return
    print "Extracting into %s" % (outfolder)
    try:
        wadfile.extract(outfolder)
    except IOError, err:
        print err
    os.chdir(olddir)

def pack(srcfolder, outfile=None):
    olddir = os.getcwd()
    os.chdir(os.path.dirname(srcfolder))
    if outfile is None:
        outfile = os.path.normpath(srcfolder) + '.wad'
    elif not outfile.lower().endswith('.wad'):
        outfile += '.wad'
    print "Reading directory %s" % (srcfolder)
    try:
        wadfile = wad.fromdirectory(srcfolder)
    except IOError, err:
        print err
        exit()
    print "Saving WAD file %s" % (outfile)
    try:
        wadfile.save(outfile)
    except IOError, err:
        print err
    os.chdir(olddir)

def checkwads(): # Check if wads have already been primed.
    ope = os.path.exists
    if ope("Data/Lego.cfg") and ope("Data/Levels/") and ope("Data/World/"):
        return False #need to improve this

def primewads():
    wads = glob.glob("LegoRR[0-9].wad")
    print wads
    pass