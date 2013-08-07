import sys
import os
import requests
import zipfile


def checkperms():
    # attempt to write a file

    pass


def checkupdate():
    r = requests.get("http://doc.asdfxyz.de:81/lms/LMS.exe")
    newlen = len(r.content)
    oldlen = int(os.stat(sys.executable).st_size)
    return oldlen != newlen


def update():
    r = requests.get("http://doc.asdfxyz.de:81/lms/LMSupdater.zip")
    if not r.ok:
        return False

    updater = file('LMSupdater.zip', 'wb')
    updater.write(r.content)
    updater.flush()
    updater.close()

    zipf = zipfile.ZipFile('LMSupdater.zip')
    zipf.extract('LMSupdater.exe')
    zipf.close()
    os.remove('LMSupdater.zip')

    os.system("start LMSupdater.exe " + os.path.basename(sys.executable))
    return True


def finalize():
    os.remove('LMSupdater.exe')
    # update complete, moving on