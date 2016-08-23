import urllib
import urllib2
from bs4 import BeautifulSoup

def test():
    mylist=range(3)
    for i in mylist:
        yield i
t=test()
for i in t:
    print t
