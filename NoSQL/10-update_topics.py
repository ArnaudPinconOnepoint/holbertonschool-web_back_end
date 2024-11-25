#!/usr/bin/env python3
"""Documented"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Lists all documents in a specified MongoDB collection.
    """
    # Insert the document into the collection
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
