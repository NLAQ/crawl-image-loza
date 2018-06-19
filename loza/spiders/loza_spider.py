import scrapy

class LozaSpider(scrapy.Spider):
    name = "loza"
    start_urls = [
      "https://loza.vn/ao-so-mi-nu",
      "https://loza.vn/quan-cong-so-nu",
      "https://loza.vn/vay-dam",
      "https://loza.vn/chan-vay",
      "https://loza.vn/vest-nu",
      "https://loza.vn/ao-khoac-nu",
      "https://loza.vn/set-do",
      "https://loza.vn/thoi-trang-dao-pho"
    ]

    def parse(self, response):
      for item_link in response.css('div.category-products li.item a.product-image::attr(href)').extract():
        yield scrapy.Request(item_link, callback=self.parse_single_item)

    def parse_single_item(self, response):
      for link in response.css('div.more-views ul li a img').xpath('@src').extract():
        img_link = link.replace("thumbnail/200x280", "image/1000x")
        yield scrapy.Request(img_link, callback=self.parse_img)

    def parse_img(self, response):
      with open("image/%s" % response.url.split('/')[-1], 'wb') as f:
        f.write(response.body)
