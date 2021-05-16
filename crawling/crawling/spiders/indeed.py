import scrapy
from crawling.items import JobItem
from scrapy.spiders import Spider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import logging

logger = logging.getLogger(__name__)


class IndeedSpider(Spider):
    name = 'indeed'
    start_urls = ['https://in.indeed.com/Internship-jobs-in-Delhi']
    base_url = 'https://in.indeed.com/'
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths='//a[@data-tn-element="next-page"]',
                           deny=('/my/mysearches', '/preferences', '/advanced_search', '/my/myjobs')),
             callback="parse_page", follow=True),)

    def parse(self, response):
        self.logger.info('Parse called on %s', response.url)
        for job in response.xpath('.//*[@data-tn-component="organicJob"]'):
            item = JobItem()
            item['title'] = job.xpath('.//a[@data-tn-element="jobTitle"]/@title[1]').extract_first(),
            item['company'] = job.xpath(".//span[@class='company']//a/text()").extract_first(),
            item['salary'] = job.xpath(".//span[@class='company']//a/text()").extract_first(),
            item['location'] = job.xpath('.//span[@class="location accessible-contrast-color-location"]/text()').extract_first(),
            item['url'] = self.base_url + str(job.xpath(".//h2[@class='title']//a/@href").extract_first())
            yield item

        next_page_url = response.css('#resultsCol > nav > div > ul > li > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
