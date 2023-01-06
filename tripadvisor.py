import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector 


class tripadvisor(scrapy.Spider):
    name = 'tripadvisor'

    start_urls = ['https://www.tripadvisor.es/Hotels-g187323-Berlin-Hotels.html','https://www.tripadvisor.es/Hotels-g187323-oa30-Berlin-Hotels.html']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    def parse(self, response): 
        yield scrapy.Request(response.url, callback=self.parse_details)
                   

    def parse_details(self, response):
       for link in response.css('div.bodycon_main').css('div.ui_column.is-8.main_col.allowEllipsis'):
            linkb=link.css('div.listing_title').css('a::attr(href)').get()
            name=link.css('div.listing_title').css('a::text').get()
            mainurl=response.url 
            yield {
                'link': linkb,
                'name': name
            }
        
        