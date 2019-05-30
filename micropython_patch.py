"""
Patch for micropython-shutil to implement some shutil methods correctly/natively
"""
import os
import shutil
import sys


if sys.implementation.name == "micropython":

    def copytree(src, dst):
        # Shim for copytree on micropython. There's no API in the micropython
        # lib for chmod or equivalent, so we use the system cp util.
        os.makedirs(dst)
        res = os.system("cp -a '{0}/.' '{1}/'".format(src, dst))
        if res != 0:
            raise Exception("Error code while executing cp: {0}".format(res))
        return dst

    def rmtree(dirname):
        # rmtree in micropython v1.9.4 breaks on directories so use
        # an os call to "rm -rf" to remove the directory.
        res = os.system("rm -rf {0}".format(dirname))

        if res != 0:
            raise Exception("Error code while executing 'rm -rf {0}': {1}".format(dirname, res))

    shutil.copytree = copytree
    shutil.rmtree = rmtree
