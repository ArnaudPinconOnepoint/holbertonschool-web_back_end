#!/usr/bin/env python3
from pymongo import MongoClient


def list_all(mongo_collection):
    # Find all documents in the collection and return them as a list
    documents = list(mongo_collection.find())
    return documents
