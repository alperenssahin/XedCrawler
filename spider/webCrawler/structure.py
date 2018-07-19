class Adresse:
    def __init__(self, url, rule={}, childe=[]):
        self.url = url
        self.rule = rule
        self.childe = childe


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

