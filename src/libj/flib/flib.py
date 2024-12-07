import os
import math

from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum, unique, auto


class Flib:
    video_exts = [".mp4", ".mkv", ".avi", ".flv", ".wmv", ".mov", ".webm", ".vob", ".3gp", ".3g2", ".m4v", ".mpg", ".mpeg", ".m2v", ".m4v", ".f4v", ".f4p", ".f4a", ".f4b"]
    image_exts = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp", "svg", "svgz", "ico", "jng", "wbmp", "cur", "heif", "heic", "avif", "apng"]
    jfilelist = []

    def __init__(self):
        self.src_filelist = []

    def get_jfilelist(self):
        return self.jfilelist

    def set_jfilelist(self,
                     src_dir_path,
                     dst_dir_path):
        
        for (src_dirpath, src_dirnames, src_filenames) in os.walk(src_dir_path):
            for src_filename in src_filenames:
                src_file = os.path.join(src_dirpath, src_filename)
                src_ext = Path(src_file).suffix.lower()
                src_size = os.path.getsize(src_file)
                #src_relpath = os.path.relpath(src_file, src_dir_path)
                src_relpath = src_dirpath.replace(src_dir_path, "")
                dst_path = os.path.join(dst_dir_path, src_relpath[1:])
                
                self.jfilelist.append(JFile(src_file,
                                                dst_path, src_filename, src_ext, FStatus.INCOMING, FExt.NOT_FILTERED,
                                                src_size))
                
    def set_jfile_filename(self, jfile, filename):
        jfile.filename = filename

        return jfile

    def classify_jfilelist_extension(self):
        for jfile in self.jfilelist:
            if jfile.filename[0] == ".":
                jfile.fext = FExt.NOT_FILTERED

                continue

            if jfile.extension in self.video_exts:
                jfile.fext = FExt.VIDEO
            elif jfile.extension in self.image_exts:
                jfile.fext = FExt.IMAGE
            else:
                jfile.fext = FExt.NOT_FILTERED


    def print_jfilelist(self,
                        in_jfilelist=jfilelist):
        for jfile in in_jfilelist:
            print("################JFILE################")
            print("SRC_PATH: ", jfile.src_path)
            print("DST_PATH: ", jfile.dst_path)
            print("FILENAME: ", jfile.filename)
            print("EXTENSION: ", jfile.extension)
            print("FSTATUS: ", jfile.fstatux)
            print("FEXT: ", jfile.fext)
            print("SRC_SIZE: ", self.convert_size(jfile.src_size))

    def is_video_jfile(self, jfile):
        if (jfile.fext == FExt.VIDEO):
            return True
        else:
            return False
        
    def is_image_jfile(self, jfile):
        if (jfile.fext == FExt.IMAGE):
            return True
        else:
            return False
        
    def is_not_filtered_jfile(self, jfile):
        if (jfile.fext == FExt.NOT_FILTERED):
            return True
        else:
            return False
    
    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)

        return "%s %s" % (s, size_name[i])
    
    def get_product_name(self, filename):
        product_name = None
        filesplitlist = filename.split("@")

        if len(filesplitlist) > 1:
            product_name = filesplitlist[1]

        return product_name


@unique
class FStatus(Enum):
    INCOMING = auto()
    OUTGOING = auto()
    DELETED = auto()


@unique
class FExt(Enum):
    VIDEO = auto()
    IMAGE = auto()
    NOT_FILTERED = auto()
    DIRECTORY = auto()


@dataclass
class JFile:
    src_path: str
    dst_path: str
    filename: str
    extension: str
    fstatux: FStatus
    fext: FExt
    src_size: int