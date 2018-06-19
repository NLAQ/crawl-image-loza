import scrapy

class LozaCategorySpider(scrapy.Spider):
    name = "loza-category"
    start_urls = [
      'https://loza.vn/'
    ]

    def parse(self, response):
      for page_link in response.css('#nav ol li a::attr(href)').extract():
          yield {
            'link' : page_link
          }
