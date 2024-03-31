from pymongo import MongoClient


class MongoDBDao:
    def __init__(self):
        self.client = MongoClient("mongodb", 27017)
