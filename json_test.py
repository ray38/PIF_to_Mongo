# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:28:35 2017

@author: ray
"""

import json
from decimal import Decimal
 
d = {}
d["Name"] = "Luke"
d["Country"] = "Canada"
 
#print json.dumps(d, ensure_ascii=False)
with open('data.json', 'w') as outfile:
    json.dump(d, outfile)
    
with open('data.json', 'r') as outfile:
    data = json.load(outfile)
    
print(data)