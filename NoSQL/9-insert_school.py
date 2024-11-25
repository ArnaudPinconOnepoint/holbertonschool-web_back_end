#!/usr/bin/env python3
"""Documented"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Lists all documents in a specified MongoDB collection.
    """
    # Insert the document into the collection
    result = mongo_collection.insert_one(kwargs)
    
    # Return the _id of the inserted document
    return result.inserted_id
