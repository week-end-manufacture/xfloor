import os
import argparse

from libj.flib.flib import Flib


def main():
    print("TEST")
    flib_instance = Flib()

    flib_instance.fget_filelist("./", "/home/roberto/Downloads")

if __name__ == "__main__":
    main()