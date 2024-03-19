from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://dmytroostrenko:DRZ105T6tvRVV0Sh@cluster0.gjov9oo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    db = client.dj

    return db



