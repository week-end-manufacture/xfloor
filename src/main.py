import os
import argparse

from dotenv import load_dotenv
from libj.flib.flib import Flib


def main():
    # Load environment variables from .env file
    load_dotenv()

    xfloor_version = os.getenv('XFLOOR_VERSION')

    parser = argparse.ArgumentParser(prog='xfloor', description='Across floor file transfer')
    parser.add_argument("-i", "--src_dir_path", help="Source directory path", action="store")
    parser.add_argument("-o", "--dst_dir_path", help="Destination directory path", action="store")
    parser.add_argument("-v", "--version", help="Version", action="version", version='%(prog)s version ' + xfloor_version + ', built with Homebrew')
    args = parser.parse_args()
    
    if (args.src_dir_path != None and args.dst_dir_path != None):
        src_dir_path = args.src_dir_path
        dst_dir_path = args.dst_dir_path
    else:
        return (-1)

    flib_instance = Flib()

    flib_instance.set_jfilelist(src_dir_path, dst_dir_path)
    flib_instance.classify_jfilelist_extension()
    flib_instance.print_jfilelist()

    jfilelist = flib_instance.get_jfilelist()

    for jfile in jfilelist:
        flib_instance.get_product_name(jfile.filename)

if __name__ == "__main__":
    main()