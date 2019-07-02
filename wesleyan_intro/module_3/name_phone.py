#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:48:51 2018

@author: DocLJN
"""

import sys
import csv

# open the csv file here

filename = sys.argv[1]
file = open(filename, 'w')
    
while True:
    nextname = input("Enter a friend's name, press return to end: ")
    if nextname == "":
        break              # break jumps out of the loop
    
    nextphone = input("Enter the friend's phone number: ")
    
    print(nextname)
    print(nextphone)
    
    option = input("Is this correct? y/n ")
    
    if option == 'y':
    
        entry = [nextname, nextphone]
        
        csv.writer(file).writerow(entry)
        
        print('Added',nextname, nextphone)
    else:
        print('Next: ')
    
    # add lines here to build a row (that is, a list) and append these
    # two pieces of data to it.  Write to the csv file
    
# don't forget to close the csv file
file.close()
