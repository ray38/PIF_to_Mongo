# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:16:32 2017

@author: ray
"""

import os
from dfttopif import directory_to_pif
import pprint
from pymongo import MongoClient

from mongo_utils import *


def DFT_spider(database = 'PIFs', collection = 'DFT', username = None, password = None):
    
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()
    
    for root, dirs, files in os.walk(".", topdown=False):
        for directory in dirs:
            try:
                data = directory_to_pif(os.path.join(root,directory))
                post = data.as_dictionary()
                path = os.path.abspath(os.path.join(root,directory))
                post['user_created'] = username
                post['path'] = path
                pp.pprint('succeed: ' + path)
                pp.pprint(post)
                collection.insert_one(post)
                
            except:
                pass
    
    return

def DFT_query(database = 'PIFs', collection = 'DFT', query = {}, username = None, password = None):
    result = []
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()
    for post in collection.find(query):
        pprint.pprint(post)
        result.append(post)
    return result

if __name__ == "__main__":
    DFT_spider(database = 'PIFs', collection = 'DFT')
    DFT_query(database = 'PIFs', collection = 'DFT', query = {})
#for post in collection.find():
#    pprint.pprint(post)