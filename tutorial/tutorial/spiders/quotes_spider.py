import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.nytimes.com/2017/11/17/us/ohio-state-fraternities.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = response.css('body')
        paragraphs = body.css('p.story-body-text a::attr(href)')
        links = paragraphs.extract()
        for link in links:
            yield scrapy.Request(link, callback = self.parse)
