import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

class Adresse(ObjectId, MongoClient,os):

    def __init__(self, adresseID):
        self.adresseID = adresseID
        self.item = self.findAdresseByID(adresseID)
        self.rules = self.item['rules']

    def ruleGenerator(self):
        # generate rules for scrapy crawler
        rules = []
        for rule in self.rules:
            str = ''
            if rule['target']:
                str += '//%s' % rule['target']
                # print(str)
            else:
                return 0

            if rule['attribute']:
                att = list(rule['attribute'])
                str += '[contains(@%s,"%s")]/' % (att[0], rule['attribute'][att[0]])
            else:
                str += '/'
                # print(str)
            for x in rule['children']:
                str += '%s/' % x
                # print(str)
            if rule['get'] == 'text':
                str += 'text()'
                # print(str)
            else:
                str += '@%s' % rule['get']
                # print(str)
            rules.append(str)
        return rules

    def findAdresseByID(self, ID):
        collection = self.getCollection()
        item = collection.find_one({'_id': ObjectId(ID)})
        return item

    def getCollection(self):
        client = MongoClient()
        db = client.xed
        collection = db.adresse
        return collection

    def print(self):
        print(self.item)


class Crawl(Adresse):
    # 'd' ----> insert to database
    # 'w' ----> crete txt file
    # 'wd' ---> both

    # def __init__(self, type):
    #     if type == 'd':
    #         #...
    #         self.database = True
    #         self.writer = False
    #         #log:saving system : database
    #     elif type == 'w':
    #         #...
    #         self.writer = True
    #         self.database = False
    #         #log:saving system : write to file
    #     else:
    #         #...
    #         self.writer = True
    #         self.database = True
    #         #log:saving system : database - write to file


    def getHttpResponse_file(self,URL):
        #call bash script
        tmp_dir = os.getcwd()
        os.chdir('/scrapy')
        #call bash


        os.chdir(tmp_dir)
        return

