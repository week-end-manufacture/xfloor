import urllib.request

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
        html = urllib.request.urlopen(json_page_url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    def get_product_name(self, input_str):
        product_name = None
        filesplitlist = input_str.split("@")

        if len(filesplitlist) > 1:
            product_name = filesplitlist[1]
            product_name = product_name.replace("-", "")
            product_name = product_name.lower()

        return product_name