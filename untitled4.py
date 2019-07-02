#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 16:57:46 2019

@author: DocLJN
"""

import pprint

object = {'Name': 'Zara', 
          'Age': 7, 
          'Class': 'First',
          'Likes': {
                      'one': 'dogs',
                      'two': 'cats'
                  }
          }

pprint.pprint(object)

f = open('test.txt','a+')
f.write('Hello World\n')
f.close()