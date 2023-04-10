#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    log = []
    for i in collection.find({}):
        log.append(i)
    print("{} logs".format(len(log)))
    print("Methods:")
    get = []
    post = []
    put = []
    patch = []
    dell = []
    for i in collection.find({"method": "GET"}):
        get.append(i)
    print("\tmethod GET: {}".format(len(get)))
    for i in collection.find({"method": "POST"}):
        post.append(i)
    print("\tmethod POST: {}".format(len(post)))
    for i in collection.find({"method": "PUT"}):
        put.append(i)
    print("\tmethod PUT: {}".format(len(put)))
    for i in collection.find({"method": "PATCH"}):
        patch.append(i)
    print("\tmethod PATCH: {}".format(len(patch)))
    for i in collection.find({"method": "DELETE"}):
        dell.append(i)
    print("\tmethod DELETE: {}".format(len(dell)))

    stat = []
    for i in collection.find({"path": "/status"}):
        stat.append(i)
    print("{} status check".format(len(stat)))
