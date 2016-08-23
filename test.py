import urllib
import urllib2
from bs4 import BeautifulSoup


def begin(self,geturl):
    self.geturl = geturl
    soup = BeautifulSoup(urllib.urlopen(geturl), "html.parser")
    for url in soup.find_all("a"):
        print url.get('href')
        endurl=url.get('href')
        try:
            if endurl=='http://mall.csdn.net/':
                return
            else:
                begin(endurl)
        except:
            return


if __name__ == '__main__':
    surl = 'http://www.csdn.net/'
    begin(surl)
