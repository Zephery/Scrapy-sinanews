# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class SinanewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link=Field()
    category=Field()
    title=Field()
    author=Field()
    date=Field()
    content=Field()

