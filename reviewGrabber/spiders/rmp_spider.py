import re
import scrapy
from scrapy.selector import Selector
from reviewGrabber.items import ReviewItem

class rmpSpider(scrapy.Spider):
    name = "rmp"
    allowed_domains = ["ratemyprofessors.com"]
    #Setting up to crawl 1 professor
    start_urls = [
        'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=951644'
    ]

    def parse(self, response):        
    	#Grabs content for 20 reviews inside reviews
    	reviews= response.xpath('//tr[@id]')
    	profFirstName=response.xpath('//*[@id="mainContent"]/div[1]/div[1]/div[2]/div[1]/h1/span[1]/text()').extract()[0].encode('utf-8')
    	profLastName=response.xpath('//*[@id="mainContent"]/div[1]/div[1]/div[2]/div[1]/h1/span[3]/text()').extract()[0].encode('utf-8').strip(' \r\n')
    	profName=profFirstName+' '+profLastName
    	#Loops through reviews, extracts each component into item.
    	#These are all lists, so [0] is needed to grab the unicode object, then encode is used to convert it to a string
    	for review in reviews:
    		print('new one')
    		item = ReviewItem()
    		item['professor']=profName
    		item['date']=review.xpath('td[1]/div[1]/text()').extract()[0].encode('utf-8')
    		item['course']=review.xpath('td[2]/span[1]/span/text()').extract()[0].encode('utf-8')
    		item['comment']=review.xpath('td[3]/p/text()').extract()[0].encode('utf-8').strip(' \r\n')
    		item['helpful']=review.xpath('td[1]/div[2]/div[2]/div[1]/span[1]/text()').extract()[0].encode('utf-8')
    		item['clarity']=review.xpath('td[1]/div[2]/div[2]/div[2]/span[1]/text()').extract()[0].encode('utf-8')
    		item['easy']=review.xpath('td[1]/div[2]/div[2]/div[3]/span[1]/text()').extract()[0].encode('utf-8')
    		yield item