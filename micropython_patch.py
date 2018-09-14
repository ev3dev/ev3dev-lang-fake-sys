"""
Patch for shutil to add copytree methods if not implemented natively
"""
import os
import shutil

if not hasattr(shutil, "copytree"):
    def copytree(src, dst):
        # Shim for copytree on micropython. There's no API in the micropython
        # lib for chmod or equivalent, so we use the system cp util.
        os.makedirs(dst)
        res = os.system("cp -a '{0}/.' '{1}/'".format(src, dst))
        if res != 0:
            raise Exception("Error code while executing cp: {0}".format(res))
        return dst

    shutil.copytree = copytree
