from distutils.core import setup
import sys
import os
import shutil
import zipfile
import py2exe
import LMS

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 1,
            'dll_excludes': ['w9xpopen.exe'],
            'excludes': ['email']
            }},
    console=[{'script': 'LMS.py', 'icon_resources': [(1, 'LMSicon32.ico')]}],
    version=LMS.VERSION,
    zipfile=None,
)
shutil.rmtree(r'C:\Users\Daniel\Documents\GitHub\lms-lrr-modding-system\build')

os.chdir('dist/')
os.remove("LMS.zip")
z = zipfile.ZipFile("LMS.zip", 'w')
z.write('LMS.exe', compress_type=zipfile.ZIP_DEFLATED)
z.close()