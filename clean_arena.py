#!/usr/bin/env python3

import os.path
import shutil
import micropython_patch


def clean_arena():
    root = os.path.dirname(__file__)
    try:
        shutil.rmtree(os.path.join(root, 'arena'))
    except OSError:
        pass

if __name__ == '__main__':
    clean_arena()
