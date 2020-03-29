# -*- coding: utf-8 -*-
import scrapy
import csv

class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/',]
                  #'https://www.qiushibaike.com/text/page/2/',]

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'qiushi-{}.csv'.format(page)
        with open(filename, 'w') as f:
            articles = response.css('.article')
            for article in articles:
                text = article.css('.text::text').extract()[0]
                author = article.css('.author::text').extract()[0]
                tags = article.css('.tag::text').extract()
                f.write(f'{text}\t{author}\t{tags}\n')
