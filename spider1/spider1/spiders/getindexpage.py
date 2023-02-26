import scrapy


class QuotesSpider(scrapy.Spider):
    name = "getindx"

    def start_requests(self):
        urls = [
           'http://172.18.58.80/snow/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        page = response.url.split("/")[-2]
        filename = f'response.css'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

