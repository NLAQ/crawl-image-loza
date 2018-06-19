import scrapy

class LozaCategorySpider(scrapy.Spider):
    name = "single-item"
    start_urls = [
      'https://loza.vn/ls770-ao-so-mi-hoa-tiet-tay-lung'
    ]

    def parse(self, response):
      for link in response.css('div.more-views ul li a img').xpath('@src').extract():
        img_link = link.replace("thumbnail/200x280", "image/1000x")
        yield scrapy.Request(img_link, callback=self.parse_img)
        # yield {
        #   'link' : link.replace("thumbnail/200x280", "image/1000x")
        # }
    def parse_img(self, response):
      with open("image/%s" % response.url.split('/')[-1], 'wb') as f:
        f.write(response.body)
