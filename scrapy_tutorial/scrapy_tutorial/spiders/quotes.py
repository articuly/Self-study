# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    # 定义爬虫名，必须唯一
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  'http://quotes.toscrape.com/page/2/', ]

    # 处理返回的结果
    def parse(self, response):
        page=response.url.split('/')[-2]
        filename='quotes-{}.txt'.format(page)
        with open(filename, 'w') as f:
            quotes=response.css('.quote')
            for quote in quotes:
                text=quote.css('.text::text').extract()[0]
                author=quote.css('.author::text').extract()[0]
                tags=quote.css('.tag::text').extract()
                f.write(f'{text}\t{author}\t{tags}\n')