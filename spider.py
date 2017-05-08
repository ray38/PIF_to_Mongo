# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:16:32 2017

@author: ray
"""

import os
from dfttopif import directory_to_pif
import pprint

pp = pprint.PrettyPrinter()

for root, dirs, files in os.walk(".", topdown=False):
    for directory in dirs:
        try:
            data = directory_to_pif(os.path.join(root,directory))
            
            pp.pprint('succeed: ' + os.path.join(root,directory))
            
        except:
            pprint('failed')