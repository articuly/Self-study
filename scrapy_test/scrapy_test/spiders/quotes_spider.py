import scrapy


class QuotesSpider(scrapy.Spider):
    # 定义爬虫名，必须唯一
    name = 'quotes'

    # 定义返回请求的链接
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/2/',
                'http://quotes.toscrape.com/page/3/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # 处理返回的结果
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
