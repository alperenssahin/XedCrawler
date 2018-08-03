
import codecs
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    # Your spider definition
    name = "orumcuk"

    def start_requests(self):

        for x in range(1, 10):
            yield scrapy.Request('https://www.gittigidiyor.com/oto-yedek-parca-aksesuar/lastik-jant-ekipmanlar?sf=%d' %  x, callback=self.parse)

    def parse(self, response):

        self.file = codecs.open('gg_s.txt', 'a', encoding="utf-8")
        for h4 in response.xpath('//h4/span/text()').extract():
            str = '%s' % h4
            self.file.write(str + ';\n')
        self.file.close()

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_DELAY' : 1
})

process.crawl(MySpider)
process.start() # the script will block here until the crawling is f