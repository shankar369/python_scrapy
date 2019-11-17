# -*- coding: utf-8 -*-
import scrapy


class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    #allowed_domains = ['https://www.zara.com/in/']
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

    start_urls = ['https://www.zara.com/in/']
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'final_data.csv'
    }
    def get_product_data(self,response):
        image_url = response.xpath("//a[@class='_seoImg main-image']/@href").extract_first()
        product_name = response.meta['name']
        product_price = response.meta['price']
        #print(image_url,'\n',product_name,'\n',product_price,'\n','*************\n\n')
        yield {
            'product_name':product_name,
            'product_price':product_price,
            'product_image':image_url,
            'product_url':response.url
        }


    def get_data(self,response):
        # print(response.text)
        li_elements = set(response.xpath("//li[contains(@class, 'product') and contains(@class, '_product')]"))
        for element in li_elements:
            product_page = element.xpath(".//a[@class='item _item']/@href").extract_first()
            product_price = element.xpath(".//div[@class='price _product-price']//span/@data-price").extract_first()
            product_name = element.xpath(".//a[@class='name _item']/text()").extract_first()
            yield scrapy.http.Request(url = response.urljoin(product_page),callback = self.get_product_data, meta={'price': product_price,'name':product_name})
            # print(element.xpath(".//a[@class='item _item']/@href").extract_first(),"*****************link")
            # print(element.xpath(".//a[@class='name _item']/text()").extract_first(),"*****************name")
            
            # print(element.xpath(".//img[contains(@class, 'product-media') and contains(@class, '_imageLoaded')]").extract_first(),"*****************photo_url")
            # print(element.xpath(".//div[@class='price _product-price']//span/@data-price").extract_first(),"*****************price")
        print(len(li_elements),"length******************")
    def parse(self, response):
        # print(response.text,"**********")
        links = set(response.xpath("//a[@class='_category-link menu-item__category-link']/@href").extract())

        print("************\n",links)
        for link in links:
            yield scrapy.http.Request(url = response.urljoin(link),callback = self.get_data)
            pass
