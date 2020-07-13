from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cotacao"]


def save(collection_name, value):
    collection = db[collection_name]
    collection.insert_one(value)
