# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:57:55 2017

@author: ray
"""

from pymongo import MongoClient
import sys


#client = MongoClient("mongodb://xlei38:`Kuyue5689740@54.201.152.64/PIFs")
#db=client['PIFs']
#collection = db['test']
#client = MongoClient('localhost', 27017)


def get_Client_uri():
    if sys.version_info[0] == 3:
        username = input('user name: ')
        password = input('password: ')
    else:
        username = raw_input('user name: ')
        password = raw_input('password: ')
        
    return "mongodb://" + username + ":" + password + "@54.201.152.64/PIFs", username, password