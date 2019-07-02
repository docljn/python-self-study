# - print_file.py *- coding: utf-8 -*-
""" Opens file and prints its contents line by line. """

import sys     # we need this library to deal with operating system

filename = sys.argv[1]

infile = open(filename)

outfilename = sys.argv[2]

outfile = open(outfilename,'w')

for line in infile:
    outfile.write(line) 

infile.close()
outfile.close()
