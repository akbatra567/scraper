import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import IndeedItem

class IndeedSpider(scrapy.Spider):
    name='indeed_jobs'
    start_urls = ['https://in.indeed.com/jobs?q=Internship&l=Delhi']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@data-tn-element="next-page"]'), deny=('/my/mysearches', '/preferences', '/advanced_search','/my/myjobs')), callback="parse_page", follow=True),)
    # def parse(self, response):
    #     SET_SELECTOR = '.jobsearch-SerpJobCard'
    #     for jobListing in response.css(SET_SELECTOR):
    #         # Yield is necessary to return scraped data.
    #         yield {
    #             # And here you get a value from each job.
    #             'company': jobListing.xpath('.//span[@class="company"]/a/text()').get('').strip()
    #         }

    def parse(self, response):
        for job in response.xpath('.//*[@data-tn-component="organicJob"]'):
            item = IndeedItem()
            item['job_title'] = job.xpath('.//a[@data-tn-element="jobTitle"]/@title[1]').extract(),
            item['company'] = job.xpath(".//span[@class='company']//a/text()").extract(),
            item['salary'] = job.xpath(".//span[@class='company']//a/text()").extract(),
            # item['date'] = job.xpath('.//span[@class="cmp-ReviewAuthor"]/text()')[-1].extract(),
            item['location'] = job.xpath('.//span[@class="location accessible-contrast-color-location"]/text()').extract(),
            item['link'] = job.xpath(".//h2[@class='title']//a/@href").extract()
            yield item
        next_page_url = response.css('#resultsCol > nav > div > ul > li > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)