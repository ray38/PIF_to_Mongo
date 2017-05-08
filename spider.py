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


def DFT_spider():

    user_uri, username, password = get_Client_uri()
    client = MongoClient(user_uri)
    db=client['PIFs']
    #posts = db.posts
    collection = db['DFT']
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

if __name__ == "__main__":
    DFT_spider()
#for post in collection.find():
#    pprint.pprint(post)