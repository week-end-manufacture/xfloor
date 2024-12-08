import os
import urllib.request

from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


class WebLib:
    url = None

    def __init__(self, url):
        self.url = url

    def get_title(self):
        html = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
class R18(WebLib):
    def get_title(self):
        html = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title
    
    def get_json_page(self,
                 product_name):
        json_page_url = "https://r18.dev/videos/vod/movies/detail/-/combined=%s/json" % product_name

        try:
            html = urllib.request.urlopen(json_page_url)
            soup = BeautifulSoup(html, 'html.parser')
            return soup.string
        except HTTPError as e:
            print(f"HTTP error occurred: {e.code} - {e.reason}")

            return None
        except URLError as e:
            print(f"URL error occurred: {e.reason}")

            return None
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

            return None
    
    def get_fanart(self,
                   image_url,
                   dst_dir_path):
        dst_file_path = os.path.join(dst_dir_path, "fanart.jpg")

        if not os.path.exists(dst_dir_path):
            os.makedirs(dst_dir_path)

        try:
            urllib.request.urlretrieve(image_url, dst_file_path)
        except HTTPError as e:
            print(f"HTTP error occurred: {e.code} - {e.reason}")
        except URLError as e:
            print(f"URL error occurred: {e.reason}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    
    def get_product_name(self, input_str):
        product_name = None
        filesplitlist = input_str.split("@")

        if len(filesplitlist) > 1:
            product_name = filesplitlist[1]
            product_name = product_name.split(".")[0]
            product_name = product_name.replace("-", "")
            product_name = product_name.lower()

        return product_name