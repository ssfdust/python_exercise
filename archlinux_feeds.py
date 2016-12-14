import requests
from html.parser import HTMLParser
import re

class feed_url_parser(HTMLParser):

    """get all the feed urls"""

    def __init__(self):
        """TODO: to be defined1. """
        HTMLParser.__init__(self)

        self.urls = []
        self.handletag = 'a'
        self.processing = 0
        self.tmp_url = ''

    def handle_starttag(self, tag, attrs):
        if tag == self.handletag:
            self.processing = 1
            for name, value in attrs:
                if name == 'href':
                    self.tmp_url = value

    def handle_data(self, data):
        if self.processing == 1:
            if data == 'Feed':
                self.urls.append(self.tmp_url)

    def handle_endtag(self, tag):
        if self.processing == 1:
            self.processing = 0


class Archlinux_feeds(object):

    """Docstring for Archlinux_feeds. """

    def __init__(self):
        """TODO: to be defined1. """
        self.url = ''

    @property
    def feeds(self):
        return self.data

    @feeds.setter
    def feeds(self, url):
        self.url = url
        print(url)
        page_data = self.get_content(url)
        self.data = (feed_url for feed_url in self.get_feed_urls(page_data))
        
    def get_feed_urls(html):
        parser = feed_url_parser()
        parser.feed(html)
        url_head = "https://www.archlinux.org"
        urls = parser.urls
        urls_copy = urls
        url_regex = re.compile(r'^http[s]:\/\/.*', re.DOTALL)
        for i, url in enumerate(urls):
            if not re.search(url_regex, url):
                urls_copy[i] = url_head + url
                
        return urls_copy

    def get_content(url):
        archfeed = requests.get(url)
        archfeed.encoding = 'utf-8'
        html = archfeed.text
        return html

