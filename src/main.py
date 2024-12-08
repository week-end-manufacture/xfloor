import os
import argparse

from libj.filelib import FileLib
from libj.jsonlib import JsonLib
from libj.weblib import *
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

    url_list = conflib_instance.get('URL_LIST', [])

    if len(url_list) > 0:
        if ("R18" in url_list):
            r18_instance = R18(url_list["R18"])

            for jfile in video_jfilelist:
                filename = jfile.filename
                product_name = r18_instance.get_product_name(filename)

                print(product_name)
                
                json_page = r18_instance.get_json_page(product_name)

                if json_page == None:
                    continue

                jsonlib_instance = JsonLib(json_page)
                actress_name = jsonlib_instance.get("actresses")[0].get("name_romaji")

                if actress_name == None:
                    continue

                jacket_image_url = jsonlib_instance.get("jacket_full_url")

                r18_instance.get_fanart(jacket_image_url, jfile.dst_path)
        else:
            print("Supported url is not in URL_LIST")

            return (-1)
    else:
        print("URL_LIST is empty")

        return (-1)

    return (1)

if __name__ == "__main__":
    main()