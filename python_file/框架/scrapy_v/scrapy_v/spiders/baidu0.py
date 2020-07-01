# -*- coding: utf-8 -*-
import scrapy
from scrapy_v.items import ScrapyVItem

class Baidu0Spider(scrapy.Spider):
    name = 'baidu0'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item=ScrapyVItem()
        print(22222222)
        print(response)
        item["title"]=response.xpath('//a/text()').extract_first()
        item["url"] = response.xpath('//a/@href').extract_first()
        print(item["title"],item["url"])
        print(11111111)

