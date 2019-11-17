# -*- coding: utf-8 -*-
import scrapy


class SpyderSpider(scrapy.Spider):
    name = 'spyder'
    allowed_domains = ['www.laughfactory.com/jokes/falmily-jokes']
    start_urls = ['https://www.laughfactory.com/jokes/falmily-jokes/']

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            yield {
                'joke_text': joke.xpath(".//div[@class='joke-text']/p").extract_first()
            }
            print(joke.xpath(".//div[@class='joke-text']/p").extract_first())
        # next_page= response.xpath("//li[@class='next']/a/@href").extract_first()
        # if next_page is not None:
        #     next_page_link= response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link, callback=self.parse)


# import scrapy


# class Spyder(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'http://quotes.toscrape.com/tag/humor/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.xpath('span/small/text()').get(),
#             }
#             print(quote.xpath('span/small/text()').get())

#         next_page = response.css('li.next a::attr("href")').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)