import os

from pathlib import Path


class Flib:
    def __init__(self):
        pass

    def fget_filelist(self,
                     src_dir_path,
                     dst_dir_path):
        
        for (src_dirpath, src_dirnames, src_filenames) in os.walk(src_dir_path):
            for src_filename in src_filenames:
                src_file = os.path.join(src_dirpath, src_filename)
                
                print(src_file)