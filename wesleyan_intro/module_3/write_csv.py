#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:21:33 2018

@author: DocLJN
"""

import sys
import csv

filename = sys.argv[1]
   
L = [['Date', 'Name', 'Notes'], 
     ['2016/1/18', 'Martin Luther King Day', 'Federal Holiday'],
     ['2016/2/2','Groundhog Day', 'Observance'], 
     ['2016/2/8','Chinese New Year', 'Observance'], 
     ['2016/2/14','Valentine\'s Day', 'Obervance'], 
     ['2016/5/8','Mother\'s Day', 'Observance'], 
     ['2016/8/19','Statehood Day', 'Hawaii Holiday'], 
     ['2016/10/28','Nevada Day', 'Nevada Holiday']]

f = open(filename, 'w', newline='')
for item in L:
    csv.writer(f).writerow(item)
f.close()
