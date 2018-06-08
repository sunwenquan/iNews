# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['http://blog.jobbole.com/all-posts/']
    start_urls = ['http://http://blog.jobbole.com/all-posts//']

    def parse(self, response):
        pass
