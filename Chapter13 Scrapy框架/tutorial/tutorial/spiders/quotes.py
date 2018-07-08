# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = QuotesItem()
            item['text'] = quote.xpath('.//span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            item['tags'] = ','.join(quote.xpath('.//a[@class="tag"]/text()').extract())
            yield item
        next = response.xpath('//ul[@class="pager"]//a/@href').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url, callback=self.parse)
