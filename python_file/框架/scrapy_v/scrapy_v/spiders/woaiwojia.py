# -*- coding: utf-8 -*-
import scrapy
from scrapy_v.items import woaiwojiai

class WoaiwojiaSpider(scrapy.Spider):
    name = 'woaiwojia'
    allowed_domains = ['https://5i5j.com/']
    start_urls = ['https://bj.5i5j.com/ershoufang/n'+str(i)+'/' for i in range(1,11)]

    def parse(self, response):
        for h in response.xpath("/html/body/div[6]/div[1]/div[2]/ul/li"):
            item = woaiwojiai()
            item["apt"]=h.xpath("div[2]/h3/a/text()").extract_first()
            item["pri"]=h.xpath("div[2]/div[1]/div/p[1]/strong/text()").extract_first()
            item["age"]=h.xpath("div[2]/div[1]/div/p[2]/text()").extract_first()
            print('1111111')
            print(item["apt"],item["pri"],item["age"])
