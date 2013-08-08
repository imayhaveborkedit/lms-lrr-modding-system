import sys
import os

import distutils.file_util
import distutils.dir_util
import stat

import wmi

import subprocess
import zipfile
import textwrap

import color


def permissions(folder):
    '''Changes file permissions so we can manipuate them'''

    # List all files in the directory,
    for root, dirnames, filenames in os.walk(folder):
        for file in filenames:
            # Get the full path to them,
            name = os.path.join(root, file)
            # and make them writable.
            os.chmod(name, stat.S_IWRITE)


def copydata(drive, location, first=True):
    '''Copies that required files from the disc'''

    # We need to perform initial installation actions
    if first:

        # If an installation already exists
        if os.path.exists(os.path.join(location, "LegoRR.exe")):
            move_install = input('''
An existing installation has been detected.
Would you like to make a backup first? {0} '''.format(r"(Y\N)"))

            # Yes, they do want to backup their existing installation
            if move_install.lower() == "y":
                print "\nWARNING: This may take a while"

                # Used to copy an existing installation
                count = 1

                # Define the new location
                new_location = "{0} Install {1}".format(location, count)

                # Another backup installation already exists
                while os.path.exists(new_location):

                    # Update the count
                    count += 1

                    # Define updated backup location
                    new_location = "{0} Install {1}".format(location, count)

                # Tell user where the backup will be located
                print '''
Your existing installation will be moved to
{0}'''.format(new_location)

                # Copy the installation
                #TODO: Catch common errors?
                distutils.dir_util.copy_tree(location, new_location)

                # Display success message
                print "\nBackup created successfully"

                print "\nRemoving original installation"

                # Update permissions so we can remove it
                permissions(location)

                # Remove the original installation, since it's been backed up
                distutils.dir_util.remove_tree(location)

                # Recreate the installation path
                os.makedirs(location)

        # Copy the CAB and HDR from the disc to the installation path
        print "\nCopying required files"
        distutils.file_util.copy_file(
            os.path.join(drive, "data1.hdr"), location)

        distutils.file_util.copy_file(
            os.path.join(drive, "data1.cab"), location)

        # Check for proper attributes, and if they match, extract the resources
        if (hasattr(sys, "frozen") and
        sys.frozen in ("windows_exe", "console_exe")):
            extractresources()

    # We need to perform final installation actions
    elif not first:

        # Display near file installation
        print "\nFinishing up installation"

        # Change the permissions on the files
        permissions(location)

        # Delete unneeded folders
        distutils.dir_util.remove_tree("DirectX6")
        distutils.dir_util.remove_tree("Registration")

        # Delete unneeded files
        os.remove("Autorun.exe")
        os.remove("Autorun.inf")
        os.remove("LegoRR.exe")
        os.remove("LegoRR.icd")
        os.remove("i5comp.exe")
        os.remove("ZD51145.DLL")
        os.remove("data1.cab")
        os.remove("data1.hdr")
        os.remove(os.path.join("Data", "Delme.dat"))
        os.remove(os.path.join("Data", "cd.key"))

         # Copy the correct Exe and ICD
        distutils.file_util.copy_file(
            os.path.join(drive, "EXE", "LegoRR.exe"), location)

        distutils.file_util.copy_file(
            os.path.join(drive, "EXE", "LegoRR.icd"), location)

        # Update permissions on the  Exe and ICD

        os.chmod(os.path.join(drive, "EXE", "LegoRR.exe"), stat.S_IWRITE)
        os.chmod(os.path.join(drive, "EXE", "LegoRR.icd"), stat.S_IWRITE)


def check():
    c = wmi.WMI()
    drive = None
    names = ["ROCKRAIDERS", "ROCK RAIDERS"]

    for cdrom in c.Win32_CDROMDrive():
        color.text(" * CD Drives: ", color.FG_GREEN)
        vname = cdrom.VolumeName if cdrom.VolumeName is not None else "[None]"

        if u'OK' in cdrom.Status and cdrom.mediaLoaded:
            color.text(u" - %s | " % cdrom.Drive, color.FG_GREEN, nl=False)
        else:
            color.text(u" - %s | " % cdrom.Drive, color.FG_LIGHT_RED, nl=False)

        if vname.upper() in names:
            color.text(vname, color.FG_GREEN)
            drive = cdrom.Drive
        else:
            color.text(vname, color.FG_LIGHT_RED)
    print;

    if drive is not None:
        print "Valid Rock Raiders disc detected"

        location = os.path.join(os.path.expanduser("~"), "Desktop",
             "LEGO Rock Raiders")

        if not os.path.exists(location):
            os.makedirs(location)
        install(drive, location)

    else:
        tex = textwrap.wrap("Could not detect a valid Rock Raiders disc. " +
        "This may because you have a different version.  If you are ABSOLUTELY" +
        "sure that the disk is a Rock Raiders disk, type the letter of the drive. " +
        "If not, then just hit enter.")
        for t in tex: print " " + t

        try: r = str(sys.stdin.readline()[:-1])
        except: r = None
        # add check for if r is a real drive.  Probably make a list of drives when checking them above
        if r:
            location = os.path.join(os.path.expanduser("~"), "Desktop",
             "LEGO Rock Raiders")

            if not os.path.exists(location):
                os.makedirs(location)
            install(r.upper()[0]+':', location)

        else: return False


# change to pushd/popd
def install(drive, location):
    copydata(drive, location, first=True)
    os.chdir(location)
    subprocess.call(["i5comp.exe", "x", "-o", "data1.cab"])
    copydata(drive, location, first=False)

    # Change the working directory back to LMS location
    os.chdir(os.path.dirname(sys.argv[0]))

    # Return True to indicate successful installation
    return True


def extractresources(location):
    zipf = zipfile.ZipFile(sys.executable)
    res = ["d3drm.dll", "i5comp.exe", "ZD51145.DLL"]
    print "Extracting resources"
    [zipf.extract(r, location) for r in res]

if __name__ == '__main__':
    check()