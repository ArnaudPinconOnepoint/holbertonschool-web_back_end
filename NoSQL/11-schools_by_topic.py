#!/usr/bin/env python3
"""Documented"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Lists all documents in a specified MongoDB collection.
    """
    # Insert the document into the collection
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
