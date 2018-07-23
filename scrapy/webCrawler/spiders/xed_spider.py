import scrapy
import codecs
from ..structure import Adresse

class MySpider(scrapy.Spider):
    name = "xed"
    #you must call xed with any adresse id
    def start_requests(self):
        self.host_url = self.getAdresseObject()
        yield scrapy.Request(self.host_url, callback=self.parse)



    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        # print(self.hell)
        # page = self.link.split("/")[-1]
        # self.file = codecs.open('gg_%s.txt' % page, 'a', encoding="utf-8")
        # for h4 in response.xpath('//h4/span/text()').extract():
        #         str = '%s' % h4
        #         self.file.write(str+';\n')
        # self.file.close()


    def getAdresseObject(self):
    # database connection... self.adresse_id
    # create object with self.adresse_id ...
        obj = Adresse('http://example.com')
        return obj

    def printData(self):
    # write data that crawled in a txt
        return

    def insertChildren(self):
    #insert childrens adresse in Adresse object.
        return