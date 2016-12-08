import feedparser
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
    print(sep)
    words = txt.split(sep)
    print(words)

    return [word.lower for word in words if word != '']

