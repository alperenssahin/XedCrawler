import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import subprocess


# class Adresse(ObjectId, MongoClient):
#
#     def __init__(self, adresseID):
#         self.adresseID = adresseID
#         self.item = self.findAdresseByID(adresseID)
#         self.rules = self.item['rules']
#
#     def ruleGenerator(self):
#         # generate rules for scrapy crawler
#         rules = []
#         for rule in self.rules:
#             str = ''
#             if rule['target']:
#                 str += '//%s' % rule['target']
#                 # print(str)
#             else:
#                 return 0
#
#             if rule['attribute']:
#                 att = list(rule['attribute'])
#                 str += '[contains(@%s,"%s")]/' % (att[0], rule['attribute'][att[0]])
#             else:
#                 str += '/'
#                 # print(str)
#             for x in rule['children']:
#                 str += '%s/' % x
#                 # print(str)
#             if rule['get'] == 'text':
#                 str += 'text()'
#                 # print(str)
#             else:
#                 str += '@%s' % rule['get']
#                 # print(str)
#             rules.append(str)
#         return rules
#
#     def findAdresseByID(self, ID):
#         collection = self.getCollection()
#         item = collection.find_one({'_id': ObjectId(ID)})
#         return item
#
#     def getCollection(self):
#         client = MongoClient()
#         db = client.xed
#         collection = db.adresse
#         return collection
#
#     def print(self):
#         print(self.item)


class Crawl:
    # 'd' ----> insert to database
    # 'w' ----> crete txt file
    # 'wd' ---> both

    def __init__(self, type):
        if type == 'd':
            # ...
            self.database = True
            self.writer = False
            # log:saving system : database
        elif type == 'w':
            # ...
            self.writer = True
            self.database = False
            # log:saving system : write to file
        else:
            # ...
            self.writer = True
            self.database = True
            # log:saving system : database - write to file

    def getHttpResponse_file(self, URL):
        # call bash script
        # created tmp file into scrapy/tmpResponse.html
        # you must use this html file before call again getHttpResponse_file()

        tmp_dir = os.getcwd()
        os.chdir('scrapy/')
        print(subprocess.call(['ls']))
        # call bash
        subprocess.call(['bash', 'HttpResponse.sh', URL])
        os.chdir(tmp_dir)
        return


# obj = Crawl('d')
# obj.getHttpResponse_file('https://www.gittigidiyor.com')

# ReferenceAttr class is constructor for understand different attributes who have relation with reference attribute
# This class may create temporal data on mongodb to create a connection succeed with django-extension-scrapy

class ReferenceAttr(ObjectId, MongoClient):

    def __init__(self, type, path='', objectID=''):
        if type == 'db':
            # call generator from db
            self.generatorDB(objectID);
        if type == 'csv':
            # call generator from csv
            self.generatorCSV(path);

    def generatorDB(self, ID):
        #read ref data from database, create a reference dictionary.
        return

    def generatorCSV(self, path):
        #read ref data from csv file and create a dictionary and if you want, you may insert this dic to mongo db
        return

    def insertDB(self,obj):
        #insert obj to db
        return
    def destroy(self):
        #destroy all data on db
        return