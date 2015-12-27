import re
import scrapy
from bs4 import BeautifulSoup


class rmpSpider(scrapy.Spider):
    name = "rmp"
    allowed_domains = ["ratemyprofessors.com"]
    #Setting up to crawl 1 professor
    start_urls = [
        'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=951644'
    ]

    def parse(self, response):
    	soup=BeautifulSoup(response.body, 'lxml')
    	print("hello")
    	print(soup)