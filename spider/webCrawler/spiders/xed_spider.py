import spider
import codecs
from ..structure import Adresse

class MySpider(spider.Spider):
    name = "xed"

    def start_requests(self):

       yield spider.Request('https://www.google.com', callback=self.parse)



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
    # write data that downloaded in a txt
        return

    def ruleGenerator(self):
    #generate rulu from  Adresse object
        return

    def insertChildren(self):
    #insert childrens adresse in Adresse object.
        return