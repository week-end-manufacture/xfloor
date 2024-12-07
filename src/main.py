import os
import argparse

from libj.flib.flib import Flib


def main():
    parser = argparse.ArgumentParser(prog='xfloor', description='Across floor file transfer')
    parser.add_argument("-i", "--src_dir_path", help="Source directory path", action="store")
    parser.add_argument("-o", "--dst_dir_path", help="Destination directory path", action="store")
    
    print("TEST")
    flib_instance = Flib()

    flib_instance.fget_filelist("./", "/home/roberto/Downloads")

    flib_instance.print_jfilelist()

if __name__ == "__main__":
    main()