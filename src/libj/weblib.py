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
    
    def get_page(self):
        html = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    def get_product_name(self, filename):
        product_name = None
        filesplitlist = filename.split("@")

        if len(filesplitlist) > 1:
            product_name = filesplitlist[1]

        return product_name