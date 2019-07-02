# -problem3_6.py *- coding: utf-8 -*-
"""
Problem 3_6:
Write a program (not just a function, but a stand alone program or script) that 
reads through a file and writes another file that gives the length of each line
in the first file.  If line is the line that you've read into your program, use
line.strip("\n") to strip away the invisible newline character at the end of
each line.  
"""
import sys

infilename = sys.argv[1]
infile = open(infilename)

outfilename = sys.argv[2]
outfile = open(outfilename, 'w+')

for line in infile:
    chars = len(line.strip("\n"))
    outfile.write(str(chars)+"\n")

infile.close()
outfile.close()
