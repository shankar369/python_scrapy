# -*- coding: utf-8 -*-
import scrapy
import os

class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    start_urls = [
        'https://akanksharedhu.com/',
    ]

    def __init__(self):
        self.page_no = 1

        self.article_no = 1


    def save_file(self,name,html):

        file = open(name,'w',encoding="utf-8")
        file.write(html)
        file.close()


    def article_pages(self,response):

        
        file_name = "page-"+str(self.page_no)+"-article-"+str(self.article_no)+'.html'

        # completeName = os.path.join(save_path, file_name)
        self.save_file(file_name,response.text)
        
        self.article_no = self.article_no + 1
        pass


    def parse(self, response):
        # save_path = str(os.getcwdb())+"\\basic_html\\"
        file_name = "page-"+str(self.page_no)+'.html'

        # completeName = os.path.join(save_path, file_name)
        self.save_file(file_name,response.text)
        
        

        article_links = response.xpath('//figure/a/@href').extract()

        for article_link in article_links:
            
            yield scrapy.Request(response.urljoin(article_link),callback = self.article_pages)
        self.article_no = 1

        next_page_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        self.page_no = self.page_no + 1

