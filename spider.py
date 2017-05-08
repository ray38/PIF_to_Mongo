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


user_uri = get_Client_uri()
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
            post['path'] = os.path.abspath(os.path.join(root,directory))
            pp.pprint('succeed: ' + os.path.join(root,directory))
            pp.pprint(post)
            collection.insert_one(post)
            
        except:
            pp.pprint('failed')

for post in collection.find():
    pprint.pprint(post)