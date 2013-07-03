from distutils.core import setup
import py2exe, sys, os
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
    #data_files=['install/d3drm.dll', 'install/i5comp.exe','install/ZD51145.DLL'],
    # I needed an obscene ammount of hax to do this properly.
    version = '0.1.1',
    zipfile = None,
)
