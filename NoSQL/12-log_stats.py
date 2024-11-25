#!/usr/bin/env python3
"""Documented"""

from pymongo import MongoClient


def log_stats():
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})

    # Print the number of logs
    print(f"{total_logs} logs")

    # Methods to check in the logs
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Print the methods count
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Get the count of GET method with path = '/status'
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
