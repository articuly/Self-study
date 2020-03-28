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
        page = response.url.split('/')[-2]
        file_name = f'quotes-{page}.html'
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(file_name))
