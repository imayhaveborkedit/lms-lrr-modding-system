from distutils.core import setup
import py2exe, sys, os, shutil, zipfile
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
shutil.rmtree(r'C:\Users\Daniel\Documents\GitHub\lms-lrr-modding-system\build')

os.chdir('dist/')
z = zipfile.ZipFile("LMS.zip", 'w')
z.write('LMS.exe', compress_type=zipfile.ZIP_DEFLATED)
z.close()