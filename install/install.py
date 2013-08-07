# General imports
import sys
import os

# Copy and delete files
import distutils.file_util
import distutils.dir_util
import stat
# Detect the CD
# import wmi
wmi = None

# Extract the cab and resources
import subprocess
import zipfile

# Colored text
# from color import *
color = None

# Bit a fun. :)
from random import choice

#TODO: Clean up ALL  the code
#TODO: Comment my code


def select():
    '''Selects and checks for a valid Rock Raiders disc'''
    #TODO: Remove this part before you send it back

    drive = input("\nPlease select the root of your Rock Raiders disc: ")

    # The user did not select a disc
    if len(drive) == 0:
        print("\nNo disc was selected")
        raise SystemExit(0)

    # The disc was selected
    else:
        print(drive)
        # The file needed to confirm this is a valid disc
        valid_file = os.path.join(drive, "exe".lower(), "legorr.exe".lower())

        # The file was found, this is a valid disc
        if os.path.isfile(valid_file):
            print("\nValid Rock Raiders disc detected.")

            #TODO: Merge this code into Doc's

            # Where we will install the game to
            location = os.path.join(os.path.expanduser("~"), "Desktop",
                 "LEGO Rock Raiders")

            # Create the installation folder if we need to
            if not os.path.exists(location):
                os.mkdir(location)

            # Begin installation
            install(drive, location)

        # The file was not found, this is not a valid disc
        else:
            print("\nThat is not a valid Rock Raiders disc.")
            select()


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
                print("\nWARNING: This may take a while.")

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
                print('''
Your existing installation will be moved to
{0}'''.format(new_location))

                # Copy the installation
                #TODO: Catch common error?
                distutils.dir_util.copy_tree(location, new_location)
                # Display sucess message
                print("\Backup created sucessfully.")

                #FIXME: connect this to the actual installation
                raise SystemExit(0)


        # Otherwise, overwite the existing installation

        # Copy the CAB and HDR
        print("Copying CAB archive")
        distutils.file_util.copy_file(
            os.path.join(drive, "data1.hdr"), location)

        distutils.file_util.copy_file(
            os.path.join(drive, "data1.cab"), location)

    # We need to perform final installation actions
    elif not first:

        # Change the permissions on the files
        permissions(location)

        # Delete unneeded folders
        distutils.dir_util.remove_tree("DirectX6")
        distutils.dir_util.remove_tree("Registration")

        # Delete unneeded files
        os.unlink("Autorun.exe")
        os.unlink("Autorun.inf")
        os.unlink("LegoRR.exe")
        os.unlink("LegoRR.icd")
        os.unlink("i5comp.exe")
        os.unlink("ZD51145.DLL")
        os.unlink("data1.cab")
        os.unlink("data1.hdr")
        os.unlink(os.path.join("Data", "Delme.dat"))
        os.unlink(os.path.join("Data", "cd.key"))

         # Copy the correct Exe and ICD
        distutils.file_util.copy_file(
            os.path.join(drive, "EXE", "LegoRR.exe"), location)
        distutils.file_util.copy_file(
            os.path.join(drive, "EXE", "LegoRR.icd"), location)


#def check2():
    #c = wmi.WMI()
    #drive = None
    #for cdrom in c.Win32_CDROMDrive():
        #colors.color(" * CD Drives: ", color.FG_GREEN)
        #vname = cdrom.VolumeName if cdrom.VolumeName is not None else "[None]"

        #if u'OK' in cdrom.Status and cdrom.mediaLoaded:
            #colors.color(u" - %s | " % cdrom.Drive, color.FG_GREEN, nl = False)
        #else:
            #colors.color(u" - %s | " % cdrom.Drive, color.FG_LIGHT_RED, nl = False)

        #names = ["ROCKRAIDERS", "ROCK RAIDERS"]
        #if vname.upper() in names:
            #colors.color(vname, color.FG_GREEN)
            #drive = cdrom.Drive
        #else:
            #colors.color(vname, color.FG_LIGHT_RED)

    #if drive is not None:
        #install(drive)
    #else:
        ## print "something something ask user"
        #print("something something ask user")


def install(drive, location=None):
    '''Runs Installation Actions'''

    # Check for proper attributes, and if they match, extract the resources
    #if (hasattr(sys, "frozen") and sys.frozen in ("windows_exe", "console_exe")
     #and location is not None):
        #extractresources()

    # Extract the resources
    if location is not None:
        extractresources(location)

    # Copy the files over
    copydata(drive, location, first=True)

    # Let's have some fun with the message
    messages = ["Sight tight,", "Hold on,", "Grab your dynamite, because",
    "Be prepared for landslides, because",
    "Start building Rock Raiders HQ, because",
    "Watch for emerging Rock Monsters, because",
    "Slimy Slugs are attacking your base!"]

    # Change the working directory to the installation path
    os.chdir(location)

    # Display installation message
    print("\n{0} LEGO Rock Raiders is installing.".format(choice(messages)))

    #FIXME: Extract to proper location, no chdir needed?
    # Extract the cab
    subprocess.call(["i5comp.exe", "x", "-o", "data1.cab"])

    # Copy the Exe and ICD over, delete all the other files
    copydata(drive, location, first=False)

    # Display success message
    print('''
LEGO Rock Raiders successfully installed to
{0}'''.format(location))

    # Change the working directory back to LMS location
    os.chdir(os.path.dirname(sys.argv[0]))

    # Return True to indicate sucessful installation
    return True


def extractresources(location):
    '''Extract the DLL and CAB Resources'''

    # Open the Exe
    #zipf = zipfile.ZipFile(sys.executable)
    zipf = zipfile.ZipFile("Data.zip")

    # List of files to extract
    res = ["d3drm.dll", "i5comp.exe", "ZD51145.DLL"]

    # Extract the resources
    print("Extracting resources")
    [zipf.extract(r, location) for r in res]

select()