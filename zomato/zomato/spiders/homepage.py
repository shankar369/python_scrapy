# -*- coding: utf-8 -*-
import scrapy


class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    #user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) Safari/537.36'
    DOWNLOAD_DELAY = 2
    CONCURRENT_REQUESTS_PER_DOMAIN = 1#
    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
    #allowed_domains = ['www.zomato.com']
    start_urls = ["https://www.zomato.com"]

    def parse(self, response):
        print("***********************************")
        print(response.text)
        