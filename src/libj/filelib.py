import os
import math
import shutil

from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum, unique, auto


class FileLib:
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
                #src_relpath = src_dirpath.replace(src_dir_path, "")
                #dst_path = os.path.join(dst_dir_path, src_relpath[1:])
                
                self.jfilelist.append(JFile(src_file,
                                                dst_dir_path, src_filename, src_ext, FStatus.INCOMING, FExt.NOT_FILTERED,
                                                src_size))

    def set_jfile_dst_path(self, jfile, dst_path):
        jfile.dst_path = dst_path

        return jfile

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

    def jcopy(self,
                jfile,
                option=0):
        src_file_path = jfile.src_path
        dst_file_path = os.path.join(jfile.dst_path, jfile.filename)
        dst_file_dir = jfile.dst_path

        if (jfile.fstatus == FStatus.INCOMING):
            if not os.path.exists(dst_file_dir):
                os.makedirs(dst_file_dir)

            total_size = os.path.getsize(src_file_path)
            copied_size = 0
            buffer_size = 1024 * 1024  # 1MB

            with open(src_file_path, 'rb') as src_file, open(dst_file_path, 'wb') as dst_file:
                while True:
                    buffer = src_file.read(buffer_size)
                    if not buffer:
                        break
                    dst_file.write(buffer)
                    copied_size += len(buffer)
                    progress = (copied_size / total_size) * 100
                    print(f"\rjCopying {jfile.filename}: {progress:.2f}%", end='')

            print()  # New line after progress bar completion

            jfile.fstatus = FStatus.OUTGOING

            return jfile
        
    def junlink(self,
                jfile,
                option=1):
        src_path = jfile.src_path
        src_dir = os.path.dirname(src_path)

        if (option == 1):
            if (jfile.fstatus == FStatus.OUTGOING):
                if (os.path.isfile(src_path)):
                    os.unlink(src_path)
                
                if (os.path.isdir(src_dir)):
                    if (len(os.listdir(src_dir)) == 0):
                        os.rmdir(src_dir)

                jfile.fstatus = FStatus.DELETED
        elif (option == 2):
            if (jfile.fstatus == FStatus.OUTGOING or self.is_video_jfile(jfile) == False):
                if (os.path.isfile(src_path)):
                    os.unlink(src_path)

                if (os.path.isdir(src_dir)):
                    if (len(os.listdir(src_dir)) == 0):
                        os.rmdir(src_dir)

                jfile.fstatus = FStatus.DELETED

        return jfile

    def print_jfilelist(self,
                        in_jfilelist=jfilelist):
        for jfile in in_jfilelist:
            print("################JFILE################")
            print("SRC_PATH: ", jfile.src_path)
            print("DST_PATH: ", jfile.dst_path)
            print("FILENAME: ", jfile.filename)
            print("EXTENSION: ", jfile.extension)
            print("FSTATUS: ", jfile.fstatus)
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
    fstatus: FStatus
    fext: FExt
    src_size: int