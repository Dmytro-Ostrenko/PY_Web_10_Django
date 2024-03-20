import json
#from bson.objectid import ObjectId

from bson import ObjectId
from pymongo import MongoClient


# Підключення до MongoDB Atlas
#client=MongoClient('mongodb+srv://dmytroostrenko:DRZ105T6tvRVV0Sh@cluster0.gjov9oo.mongodb.net/hwdjango')
client = MongoClient("mongodb://localhost")
db=client.hwdjango


with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)



for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.authors.find_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })




# # Завантаження даних про авторів
# with open('authors.json', 'r') as file:
#     authors_data = json.load(file)
#     for author_data in authors_data:
#         author = Author(**author_data)
#         author.save()
#

