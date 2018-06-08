# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from iNewsRedisCrawl.items import InewsrediscrawlItem

class JobboleSpider(RedisSpider):
    name = 'jobbole'

    # start_urls = ['http://blog.jobbole.com/all-posts/']
    redis_key = 'jobbole:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(JobboleSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        posts = response.css('div.post-meta')[:10]
        for post in posts:
            item = InewsrediscrawlItem()
            item['link']=post.css('a.archive-title::attr(href)').extract_first()
            item['name'] =post.css('a.archive-title::text').extract_first()
            print(item)
            yield item

