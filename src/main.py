import os
import argparse

from libj.filelib import FileLib
from libj.jsonlib import JsonLib
from libj.weblib import *
from libj.loglib import LogLib
from libj.conflib import ConfLib
from libj.verlib import __version__


def main():
    # Initialize logger
    log = LogLib(name='xfloor').get_logger()

    # Load environment variables from JSON file
    conflib_instance = ConfLib('xfloor')
    conflib_instance.set_env_variables()

    xfloor_version = __version__

    parser = argparse.ArgumentParser(prog='xfloor', description='Across floor file transfer')
    parser.add_argument("-i", "--src_dir_path", help="Source directory path", action="store")
    parser.add_argument("-o", "--dst_dir_path", help="Destination directory path", action="store")
    parser.add_argument("-v", "--version", help="Version", action="version", version='%(prog)s version ' + xfloor_version + ', built with Homebrew')
    parser.add_argument("-s", "--settings", help="Open setting directory", action="store_true")
    args = parser.parse_args()

    if (args.settings):
        conflib_instance.open_config()

        return (1)
    
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

    url_list = conflib_instance.get('URL_LIST', [])

    if len(url_list) > 0:
        if ("R18" in url_list):
            r18_instance = R18(url_list["R18"])

            for jfile in jfilelist:

                if (flib_instance.is_video_jfile(jfile) == False):
                    continue

                filename = jfile.filename
                product_name = r18_instance.get_product_name(filename)

                print(product_name)
                
                json_page = r18_instance.get_json_page(product_name)

                if json_page == None:
                    continue

                jsonlib_instance = JsonLib(json_page)

                try:
                    actress_name = jsonlib_instance.get("actresses")[0].get("name_romaji")
                    dvd_id = jsonlib_instance.get("dvd_id")
                    release_date = jsonlib_instance.get("release_date")
                    release_date = release_date.split("-")[0]
                except IndexError:
                    print("IndexError")
                    continue

                edge_dirname = f"{dvd_id}({release_date})"

                if actress_name == None or dvd_id == None:
                    continue

                tmp_dst = os.path.join(dst_dir_path, actress_name, edge_dirname)
                jfile = flib_instance.set_jfile_dst_path(jfile, tmp_dst)

                jacket_image_url = jsonlib_instance.get("jacket_full_url")

                if (r18_instance.get_fanart(jacket_image_url, jfile.dst_path) == None):
                    print("Failed to download fanart")

                tmp_filename = f"{dvd_id}{jfile.extension}"
                jfile = flib_instance.set_jfile_filename(jfile, tmp_filename)

                flib_instance.jcopy(jfile)

            for jfile in jfilelist:    
                flib_instance.junlink(jfile, 2)
            
        else:
            print("Supported url is not in URL_LIST")

            return (-1)
    else:
        print("URL_LIST is empty")

        return (-1)

    return (1)

if __name__ == "__main__":
    main()