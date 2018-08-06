from selenium import webdriver
from pymongo import MongoClient
from bson.objectid import ObjectId
class XedCrawler(webdriver.Firefox,MongoClient,ObjectId):

    def __init__(self,ID):
        self.rulesGenerator(ID)
        self.driver =  webdriver.Firefox()
        self.url = self.ruleSet['url']

    def request(self,callback = None):
        self.driver.get(self.url)
        self.response = self.driver.find_element_by_css_selector('html').get_attribute('innerHTML')
        if callback:
            callback()

    def rulesGenerator(self,ID):

        client = MongoClient()
        self.ruleSet = client.rules.tmp.find_one({'_id': ObjectId(ID)})
        self.rules = []

        rules = self.ruleSet['rules']
        for rule in rules:
            rul = rules[rule]
            outRule = {'target': rul['target'], 'ids': rul['attribute'], 'rules': []}
            str = '/'

            if len(rul['children']) == 0:
                str += '/%s' % rul['target']
            else:
                for x in rul['children'][::-1]:
                    str += '/%s' % x
                    # print(str)
            for get in rul['get']:
                tmp = str
                if get == 'text':
                    textRule = 'string(%s[1])' % tmp
                    outRule['rules'].append(textRule)
                    # print(tmp)
                else:
                    tmp += '/@%s' % get
                    outRule['rules'].append(tmp)
                    # print(tmp)
            self.rules.append(outRule)

    def parser(self):
        from scrapy import Selector
        for rule in self.rules:
            css = '%s' % rule['target']

            if rule['ids']['id']:
                css += '#%s'% rule['ids']['id']
            if rule['ids']['class']:
                css +='.%s' % rule['ids']['class']

            obj = Selector(text=self.response).css(css).extract()

            for str in obj:
                for xrule in rule['rules']:
                    ob = Selector(text=str).xpath(xrule).extract()
                    print(ob)

    def quit(self):
        self.driver.close()
        self.driver.quit()


# # #

Xed = XedCrawler('5b684d752c88840719c87def')
Xed.request(callback=Xed.parser)
Xed.quit()
