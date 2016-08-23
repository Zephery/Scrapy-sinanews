# encoding=utf-8
import scrapy
from bs4 import BeautifulSoup
from sinanews.items import SinanewsItem


class SinaSpider(scrapy.Spider):
    name = "sinanews"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = ["http://news.sina.com.cn"]

    # start_urls = ["http://news.sina.com.cn/"]

    def parse(self, response):
        for url in response.xpath('//li/a/@href').extract():
            yield scrapy.Request(url, callback=self.parseNews)
            yield scrapy.Request(url)

    def parseNews(self, response):
        News = []
        News_url = response.xpath('//div[@class="feed-card-item"]/h2/a/@href').extract()
        News.extend([self.make_requests_from_url(url).replace(callback=self.parseSave) for url in News_url])
        return News

    def parseSave(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        item = SinanewsItem()
        judgeurl = response.url
        if str(judgeurl).__contains__('video') or str(judgeurl).__contains__('slide'):
            print ("filter video and slide")
        else:
            try:
                item["link"] = response.url
                item["category"] = response.url.split("/")[-2]
                item["title"] = soup.find('title').getText()
                item["author"] = soup.find('p', attrs={'class', 'article-editor'}).getText()
                item["date"] = soup.find('span', id='navtimeSource').getText()
                item["content"] = soup.find('div', id='artibody').getText()
            except:
                pass
            # item["date"]=unicode(response.xpath('//span[@class="time-source"]'))
            # # item["date"]=soup.find('span')
            # item["author"] = unicode(response.xpath('//p[@class="article-editor"]')).encode("GBK")
            # item["content"]=unicode(response.xpath('//div[@id="artibody"]').extract()).encode("gbk")
            # item["title"]=unicode(response.xpath('//title'))
            if "content" not in item.keys():  # 判断是否含有content
                print ("empty")
            else:
                yield item
