import scrapy
import codecs

from .Rules import Rules
class MySpider(scrapy.Spider):
    name = "simple"


    def start_requests(self):
        self.myRule = Rules('5b645c382c88840ba34d32c4')
        self.link = self.myRule.url
        yield scrapy.Request(self.link, callback=self.parse)


    def parse(self, response):
        myRules = self.myRule.ruleGenerator()
        self.file = codecs.open('crawler_test.txt' ,'a', encoding="utf-8")
        for rule in myRules:
            css = '%s#%s.%s' %(rule['target'],rule['ids']['id'],rule['ids']['class'])
            # css = '%s.%s' % (rule['target'], rule['ids']['class'])
            for rul in rule['rules']:
                for x in response.css(css).xpath(rul).extract():
                        str = '%s' % x
                        self.file.write(str+';\n')

        # TEST:css//xpath
        # for x in response.css('div#inside.main').xpath('string(//form/p/span[1])').extract():
        #         str = '%s' % x
        #         self.file.write(str+';\n')

        self.file.close()
