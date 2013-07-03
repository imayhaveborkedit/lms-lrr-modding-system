from distutils.core import setup
import py2exe, sys, os, shutil
import LMS
sys.argv.append('py2exe')
setup(
    options = {
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 1,
            'dll_excludes': ['w9xpopen.exe'],
            'excludes':['email']
            }},
    console = [{'script': 'LMS.py','icon_resources': [(1, 'LMSicon32.ico')]}],
    version = LMS.VERSION,
    zipfile = None,
)
shutil.rmtree("/build")