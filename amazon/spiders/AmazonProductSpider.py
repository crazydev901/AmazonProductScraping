# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem

class AmazonproductspiderSpider(scrapy.Spider):
    name = 'AmazonDeals'
    allowed_domains = ['amazon.com']
    start_urls = ['http://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0//']
    
    # def start_requests(self):
    #     start_urls = ['http://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0//']
    #     while True:
    #         items = scrapy.Request(url=start_urls[0], callback=self.parse)
    #         yield items
        
    def parse(self, response):
        items = AmazonItem()
        item_no = 1
        while True:
            print(item_no)
            product_name = response.xpath('//*[@id="zg-ordered-list"]/li['+ str(item_no) +']/span/div/span/a/div/text()').extract()
            product_price = response.xpath('//*[@id="zg-ordered-list"]/li['+ str(item_no) +']/span/div/span/div[2]/a/span/span/text()').extract()
            items['product_name'] = ''.join(product_name).strip()
            items['product_price'] = ''.join(product_price).strip()
            items['method'] = "Scrapy"
            if items['product_name'] == "":
                break
            yield items
            item_no += 1
        pass