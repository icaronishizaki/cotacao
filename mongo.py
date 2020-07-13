from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cotacao"]


def save(collection_name, value):
    collection = db[collection_name]
    collection.insert_one(value)


def get_all(collection_name):
    return list(db[collection_name].find({}, {'_id': 0, 'value': 1, 'date': 1}))


def get(collection_name):
    return db[collection_name].find_one({}, {'_id': 0, 'value': 1, 'date': 1})
