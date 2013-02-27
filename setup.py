from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(
    options = {
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 1
            }},
    console = [{'script': "LMS.py"}],
    #data_files=[("utils",["install/d3drm.dll", "install/i5comp.exe","install/ZD51145.DLL"])],
    zipfile = "LMS.dll",
)
