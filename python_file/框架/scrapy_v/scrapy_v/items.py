# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyVItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()


class woaiwojiai(scrapy.Item):
    apt=scrapy.Field()
    pri=scrapy.Field()
    age=scrapy.Field()