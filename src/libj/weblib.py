import urllib.request

from bs4 import BeautifulSoup


class WebLib:
    url_list = []

    def __init__(self, url_list):
        self.url_list = url_list

    def get_title(self):
        html = urllib.request.urlopen(self.url_list[0])
        soup = BeautifulSoup(html, 'html.parser')
        return soup