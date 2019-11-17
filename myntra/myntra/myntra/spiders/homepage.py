# -*- coding: utf-8 -*-
import scrapy
# import csv
# # from csv import csvwriter
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

# from time import sleep
import json
# import csv

class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    #allowed_domains = ['https://www.myntra.com/']
    start_urls = ["https://www.myntra.com"]

    def __init__(self):
        self.domain = "https://www.myntra.com"
        # self.file_name = "final_data.csv"
        # self.file = open(self.file_name)
        # self.csv_writer = csv_writer(self.file)
        # self.driver = webdriver.Chrome()
        self.file = open("product_details.json","w")



    def data_collector(self,response):
        # self.driver.get(response.url)
        # sleep(3)
        # links = self.driver.xpath('//h3[@class="product-brand"]')
        # print("****************\n\n",links,"\n\n*********************")
        # pass
        true = True
        false = False
        null = None
        print("############################################")
        required_script_tag = ""
        for script_tag in response.xpath('//script').extract():
            if("window.__myx = {" in script_tag):
                required_script_tag = script_tag
                break
        #print(script_tag)
        for word in ["<script>window.__myx = ","</script>"]:
            required_script_tag = required_script_tag.replace(word, '')

        for product_info in json.loads(required_script_tag)["searchData"]["results"]["products"]:
            print(product_info["product"])

            self.file.write(json.dumps(product_info))
            self.file.write(",")

        



    def parse(self, response):
        self.file.write("[")
        all_links = response.xpath('//a[@class="desktop-categoryLink"]/@href').extract()
        print(all_links,"****************\n\n")
        for link in all_links:
            #print("***************",self.domain+link,"************************")
            yield scrapy.http.Request(url = response.urljoin(self.domain+link),callback = self.data_collector)
        


    def __del__(self):
        self.file.write("]")
        self.file.close()
