"""
Patches for shutil to add copyfile and copytree methods if not implemented natively
"""
import os
import shutil

if not hasattr(shutil, "copyfile"):
    def copyfile(src, dst):
        with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
            shutil.copyfileobj(fsrc, fdst)

    shutil.copyfile = copyfile

if not hasattr(shutil, "copytree"):
    def copytree(src, dst):
        names = os.listdir(src)

        os.makedirs(dst)
        errors = []
        for name in names:
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if os.path.isdir(srcname):
                    copytree(srcname, dstname)
                else:
                    copyfile(srcname, dstname)
            except Error as err:
                errors.extend(err.args[0])
            except OSError as why:
                errors.append((srcname, dstname, str(why)))
        
        if errors:
            raise Error(errors)
        return dst

    shutil.copytree = copytree
