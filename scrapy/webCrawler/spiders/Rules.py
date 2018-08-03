
from pymongo import MongoClient
from bson.objectid import ObjectId



class Rules(ObjectId, MongoClient):

    def __init__(self, ruleID):
        self.FindRules(ruleID)
        self.url = self.rule['url']

    def ruleGenerator(self):
        # generate rules for scrapy crawler
        genRules = []
        rules = self.rule['rules']
        for rule in rules:
            rul = rules[rule]
            outRule = {'target':rul['target'],'ids':rul['attribute'],'rules':[]}
            str = '/'
            for x in rul['children'][::-1]:
                str += '/%s' % x
                # print(str)
            for get in rul['get']:
                tmp = str
                if get == 'text':

                    textRule = 'string(%s[1])' % tmp
                    outRule['rules'].append(textRule)
                    print(tmp)
                else:
                    tmp += '/@%s' % get
                    outRule['rules'].append(tmp)
                    print(tmp)
            genRules.append(outRule)
        return genRules

    def FindRules(self,ruleID):
        client = MongoClient()
        col = client.rules.tmp
        self.rule = col.find_one({'_id': ObjectId(ruleID)})