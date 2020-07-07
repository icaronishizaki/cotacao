import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cotacao"]
collection = mydb["Dolar"]


def save(collection, value):
    mycol = mydb[collection]

    mycol.insert_one(value)