import scrapy
import codecs

class MySpider(scrapy.Spider):
    name = "Http"


    def start_requests(self):

        yield scrapy.Request(self.url, callback=self.parse)


    def parse(self, response):
        self.file = codecs.open('tmpResponse.html','a', encoding="utf-8")
        str = '%s' % response.body.decode(response.encoding)
        self.file.write(str+';\n')
        self.file.close()
