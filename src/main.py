import os
import argparse

from dotenv import load_dotenv
from libj.filelib import FileLib
from libj.weblib import WebLib
from libj.conflib import ConfLib


def main():
    # Load environment variables from JSON file
    conflib_instance = ConfLib('../config/config.json')
    conflib_instance.set_env_variables()

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

    flib_instance = FileLib()

    flib_instance.set_jfilelist(src_dir_path, dst_dir_path)
    flib_instance.classify_jfilelist_extension()
    flib_instance.print_jfilelist()

    jfilelist = flib_instance.get_jfilelist()
    video_jfilelist = []

    for jfile in jfilelist:
        if flib_instance.is_video_jfile(jfile):
            video_jfilelist.append(jfile)

    for jfile in video_jfilelist:
        product_name = flib_instance.get_product_name(jfile.filename)

        if product_name != None:
            jfile.filename = product_name

    flib_instance.print_jfilelist(video_jfilelist)

    url_list = conflib_instance.get('URL_LIST', [])
    print("URL_LIST: ", url_list)
    weblib_instance = WebLib(url_list)
    print(weblib_instance.get_title())

    return (1)

if __name__ == "__main__":
    main()