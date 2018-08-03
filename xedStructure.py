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
            self.reference = self.generatorDB(objectID)
        if type == 'csv':
            # call generator from csv
            self.reference = self.generatorCSV(path)

    def generatorDB(self, ID):
        # read ref data from database, create a reference dictionary.
        client = MongoClient()
        db = client.reference
        collection = db.permenant
        self.reference = collection.find_one({'_id': ObjectId(ID)})
        self.post_id = ID


    def generatorCSV(self, path):
        # -*- coding: utf-8 -*-
        # read ref data from csv file and create a dictionary and if you want, you may insert this dic to mongo db
        import codecs
        a = 0

        import uuid
        def createObject(lines, startline,indx):
            global a
            a = startline
            obj = {}
            position = 1
            tmp = []
            while 1:
                if a >= len(lines):
                    break
                line = lines[a].split(';')
                for l in line:
                    if l == '' or l == '-':
                        continue
                    else:
                        t = line.index(l)
                        n = line[t + 1]
                        if n == '' or n == '-':
                            if position == t:
                                tmp.append(l)
                                break
                            else:
                                if(line.index(l) == indx):
                                    a -= 1
                                    return obj
                                else:
                                    obj[l] = createObject(lines, a + 1,line.index(l))
                                    break
                        else:
                            if l == 'value':
                                obj[l] =[]
                                obj[l].append(n)
                                obj['uID'] = uuid.uuid4()
                                tmp = obj[l]
                                break
                            else:
                                obj[l] = n
                                position = t+1
                                break
                a += 1
            return obj

        filename = path

        with open(filename, 'r', encoding="utf8", errors='ignore') as f:
            reader = f.read()
            lines = reader.split('\n')
            reff = createObject(lines, 0,99)
            # print(reff)
        return reff


    def insertDB(self):
        # insert obj to db
        client = MongoClient()
        db = client.reference
        collection = db.tmp
        self.post_id = collection.insert_one(self.reference).inserted_id



    def destroy(self):
        # destroy all data on db
        client = MongoClient()
        db = client.reference
        collection = db.permenant
        result = collection.delete_one({'_id': ObjectId(self.post_id)})
        return result

a = ReferenceAttr('csv', 'taslak_referans.csv')
print(a.reference)
a.insertDB()
