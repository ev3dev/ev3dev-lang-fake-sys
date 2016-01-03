#!/usr/bin/env python

import os
import shutil

def clean_arena():
    root = os.path.dirname(os.path.realpath(__file__))
    shutil.rmtree(os.path.join(root, 'arena'), ignore_errors=True)

if __name__ == '__main__':
    clean_arena()
