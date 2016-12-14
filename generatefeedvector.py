import feedparser
from archlinux_feeds import Archlinux_feeds
import re

def getwordcounts(url):
    """TODO: Docstring for getwordcounts.

    :url: TODO
    :returns: TODO

    """
    d = feedparser.parse(url)
    wc = {}

    for e in d.entries:
        if 'summary' in e: summary = e.summary
        else: summary = e.description

        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return d.feed.title, wc

def getwords(html):
    """TODO: Docstring for getwords.

    :html: TODO
    :returns: TODO

    """
    txt = re.sub(r'<[^>]+>', '', html)

    reg_words = re.compile(r'[^A-Z^a-z]+')
    sep = re.search(reg_words, html).group()
    words = txt.split(sep)

    return [word.lower() for word in words if word != '']

def main():
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    url = 'https://www.archlinux.org/feeds/'
    arch_feeds = Archlinux_feeds()
    arch_feeds.feeds = url
    urls = arch_feeds.feeds
    for i in urls:
        print(i)
