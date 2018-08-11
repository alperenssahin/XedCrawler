from selenium import webdriver
from pymongo import MongoClient
from bson.objectid import ObjectId


class XedCrawler(webdriver.Firefox, MongoClient, ObjectId):
    # xedCrawler is a base class who works with selenium integration
    def __init__(self, ID):
        self.rulesGenerator(ID)  # call rule from mongoDB
        self.driver = webdriver.Firefox()  # driver for selenium ---> we can change firefox read more about selenium at readme and webSite
        self.url = self.ruleSet['url']  # declaration url

    # request is initialisation of seleniyum, you are connecting to a webrowser and crawl html content,
    # you may call callback function for all request

    def simpleRequest(self):
        self.driver.get(self.url)
        self.crawledElements = []
        for par in self.rules:
            scraps = self.driver.find_elements_by_xpath(par['rule'])
            for scrap in scraps:
                for type in par['get']:  # todo:reference settings
                    if type == 'text':
                        scr = {'type': 'text', 'data': scrap.text, 'reference': {}}
                        self.crawledElements.append(scr)
                    else:
                        scr = {'type': type, 'data': scrap.get_attribute(type), 'reference': {}}
                        self.crawledElements.append(scr)

    # rulesGenerator create rule for adaptation to parser function

    def rulesGenerator(self, ID):
        import itertools
        client = MongoClient()  # DBconnection
        self.ruleSet = client.rules.tmp.find_one({'_id': ObjectId(ID)})  # DBquery
        # todo: check rules is recursive
        # todo: create follow rules and condition
        # print(self.ruleSet)
        self.rules = []

        rules = self.ruleSet['rules']
        for rule in rules:
            rul = rules[rule]
            str = '/'
            if rul['elevator'] != None:
                branch = True
                if rul['originType'] == 'unique':


                    for path, elev in itertools.zip_longest(rul['path'][::-1], rul['elevator'][::-1],fillvalue='vide'):
                        # print('%s----%s'%(path,elev))
                        if path != elev and  branch :
                            branch = False
                            str += '/%s[text()="%s"]/..' % (path['tag'],rul['text'])
                        if branch:
                            str += '/%s' % path['tag']
                            if (path['class'][0] != ''):
                                str += '[contains(@class,"%s")]' % ' '.join(path['class'])
                            # else:
                            #     if path['id'] != '':
                            #         str += '[contains(@id,"%s")]' % path['id']
                        else:
                            str += '/%s' % elev['tag']
                            if (elev['class'] != []):
                                str += '[contains(@class,"%s")]' % ' '.join(elev['class'])
                            # else:
                            #     if elev['id'] != '':
                            #         str += '[contains(@id,"%s")]' % elev['id']

            else:
                if rul['originType'] == 'unique':
                    for path in rul['path'][::-1]:
                        str += '/%s' % path['tag']
                        if (path['class'][0] != ''):
                            str += '[contains(@class,"%s")]' % ' '.join(path['class'])
                        # else:
                        #     if path['id'] != '':
                        #         str += '[contains(@id,"%s")]' % path['id']


            if rul['originType'] == 'recurrent':
                for path in rul['path'][::-1]:
                    str += '/%s' % path['tag']
            # print(str)
            ruleObj = {'rule':str,'get':rul['get'],'reference':{},'crawltype':[]}
            self.rules.append(ruleObj)

    def simpleParser(self):
        self.crawledElements = []
        for par in self.rules:
            scraps = self.driver.find_elements_by_xpath(par['rule'])
            for scrap in scraps:
                for type in par['get']: #todo:reference settings
                    if type == 'text':
                        scr = {'type':'text','data':scrap.text,'reference':{}}
                        self.crawledElements.append(scr)
                    else:
                        scr = {'type': type, 'data': scrap.get_attribute(type), 'reference': {}}
                        self.crawledElements.append(scr)


    # you must use quit for close temporal browser
    def quit(self):
        self.driver.close()
        self.driver.quit()

# # #
# There is a simple example for understand XedCrawler


Xed = XedCrawler('5b6d71842c888402bad3221c')
# Xed.rulesGenerator2('5b6d397f2c888402bad32200')
Xed.simpleRequest()
print(Xed.crawledElements)
Xed.quit()
