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
                pp.pprint('found: ' + path)
#                pp.pprint(post)
#                pp.pprint(type(path))
#                pp.pprint(path)
                pp.pprint('input query')
                temp_query = {'path': path}
                pp.pprint(' query')
                temp = collection.find(temp_query).count()
                pp.pprint('finished query')
#                pp.pprint(type(temp))
#                temp = DFT_query(database = database, collection = collection, query = {'path': str(path)}, username = username, password = password)
#                pp.pprint(str(len(temp)))                
                if temp == 0:
                    collection.insert_one(post)
                    pp.pprint('successfully inserted to database')
                else:
                    pp.pprint('director already in database: ' + path)
                    pp.pprint('delete the existing document to update')
                
            except:
                pass
    
    return

def DFT_query(database = 'PIFs', collection = 'DFT', query = {}, username = None, password = None,printout = False):
    result = []
    if username == None or password == None:
        username, password = user_authentication()
    user_uri  = get_Client_uri(username, password)
    client = MongoClient(user_uri)
    db=client[database]
    collection = db[collection]
    pp = pprint.PrettyPrinter()
    for post in collection.find(query):
        if printout == True:
            pprint.pprint(post)
        result.append(post)
    pp.pprint('total documents found: ' + str(len(result)))
    return result

if __name__ == "__main__":
    username, password = user_authentication()
    DFT_spider(database = 'PIFs', collection = 'DFT', username = username, password = password)
    DFT_query(database = 'PIFs', collection = 'DFT', query = {'path':'/gpfs/pace1/project/chbe-medford/medford-share/users/bcomer3/espresso_rutile/espresso_Rutile/2_layer_runs/N/test/esp.log'}, username = username, password = password)
#for post in collection.find():
#    pprint.pprint(post)