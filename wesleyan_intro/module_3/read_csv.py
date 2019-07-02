#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:21:33 2018

@author: DocLJN
"""

import sys
import csv

filename = sys.argv[1]
f = open(filename)
for row in csv.reader(f):
    for item in row:
        print(item,end=' ')
    print()
f.close()
