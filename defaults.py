import os
import sys


def get_root_path():
    ROOT = os.path.dirname(sys.modules['__main__'].__file__)
    with open((ROOT + '/setups_path'), 'r') as f:
        for line in f:
            ROOT_DIR = str(line.rstrip())
    if ROOT_DIR == "ROOT":
        ROOT_DIR = ROOT
    return ROOT_DIR

def get_ui_status():
    ROOT = os.path.dirname(sys.modules['__main__'].__file__)
    with open((ROOT + '/setups_UI'), 'r') as f:
        for line in f:
            START_UI = str(line.rstrip())
    return START_UI