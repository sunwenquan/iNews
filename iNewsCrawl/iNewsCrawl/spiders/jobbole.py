# -*- coding: utf-8 -*-
import scrapy
from iNewsCrawl.items import InewscrawlItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        posts = response.css('div.post-meta')[:10]
        for post in posts:
            item = InewscrawlItem()
            item['link']=post.css('a.archive-title::attr(href)').extract_first()
            item['name'] =post.css('a.archive-title::text').extract_first()
            print(item)
            yield item

