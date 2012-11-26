import re
import diff_match_patch
import os

dmp = diff_match_patch.diff_match_patch()


os.chdir(r"C:/Users/Daniel/Desktop")

def patch(user_cfg, mod_cfg):
    f = open(user_cfg, 'r+')
    user_cfg_text = f.read()
    patches = dmp.patch_make(user_cfg_text, open(mod_cfg).read())
    return patches
    results = dmp.patch_apply(patches, user_cfg_text)
    f.seek(0)
    f.write(results[0])
    f.close()
    return results[1:]


r = patch("user.cfg", "mod.cfg")
print r[0]