# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request
from urllib.parse import urlencode

from images360.items import Images360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        data = {
            'ch': 'photography',
            'listtype': 'new'
        }
        base_url = 'http://image.so.com/zj?'
        for page in range(0,50):
            data['sn'] = page*30
            # 转化为URRL的get参数
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        reslt = json.loads(response.text)
        for image in reslt.get('list'):
            item = Images360Item()
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item

