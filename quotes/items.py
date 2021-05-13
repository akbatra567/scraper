# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class IndeedItem(scrapy.Item):
    job_title =  scrapy.Field()
    company =  scrapy.Field()
    salary =  scrapy.Field()
    location = scrapy.Field() 
    link =  scrapy.Field()
    date = scrapy.Field()