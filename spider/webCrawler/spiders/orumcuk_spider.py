import spider
import codecs

class MySpider(spider.Spider):
    name = "orumcuk"


    def start_requests(self):

        for x in range(1,int(self.lmt)):
            yield spider.Request('https://www.gittigidiyor.com/%s?sf=%d' % (self.link , x), callback=self.parse)


    def parse(self, response):
        page = self.link.split("/")[-1]
        self.file = codecs.open('gg_%s.txt' % page, 'a', encoding="utf-8")
        for h4 in response.xpath('//h4/span/text()').extract():
                str = '%s' % h4
                self.file.write(str+';\n')
        self.file.close()

