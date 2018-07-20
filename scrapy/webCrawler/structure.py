class Adresse:
    def __init__(self, url, rules={}, childe=[]):
        self.url = url
        self.rules = rules
        self.childe = childe

    def ruleGenerator(self):
        #generate rules for scrapy crawler
        str = ''
        if self.rules['target']:
            str += '//%s'%self.rules['target']
            # print(str)
        else:
            return 0

        if self.rules['attribute']:
            att = list(self.rules['attribute'])
            str += '[contains(@%s,"%s")]/'%(att[0], self.rules['attribute'][att[0]])
            # print(str)
        for x in self.rules['children']:
            str += '%s/'%x
            # print(str)
        if self.rules['get'] == 'text':
            str += 'text()'
            # print(str)
        else:
            str += '@%s'%self.rules['get']
            # print(str)
        return str

# import pymongo
# from pymongo import MongoClient
#
# client = MongoClient()
# db = client.xed
#
# col = db.adresse
#
# my_adresse = col.find({'Id':'1'})
#
# for x in my_adresse:
#     print(x)
#     add = x
#
# Obj = Adresse(add['url'],add['rules'])
#
# rule = Obj.ruleGenerator()
#
# print(rule)
# mylist = [
#     Adresse('myurl2', {'dic1': 1}),
#     Adresse('c', {'dic': 'a'}),
#     Adresse('myurl2', {'dic1': 1}),
#     Adresse('c', {'dic': 'a'}),
#     Adresse('myurl2', {'dic1': 1}),
#     Adresse('c', {'dic': 'a'}),
#     Adresse('myurl2', {'dic1': 1}),
#     Adresse('c', {'dic': 'a'}),
# ]
#
# parent = Adresse('my_url', {'rulle:': 1, 'rulle2': 2}, mylist)
#
# # print(mylist['a'].rule)
# # print(mylist['b'].url)
# #
# # print(parent.childe)
# # print(parent.childe['a'].url)
#
# for x in mylist:
#     print (x)

