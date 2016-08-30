#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for threading"
 
__author__ = 'mxl'

import csv
import numpy

filename = "keys.csv"
data = []

#try:
#    with open(filename) as f:
#        reader = csv.reader(f)
#        header = reader.next()
#        data = [row for row in reader]
#except:
#    print "exception"

#if header:
#    print header
#    print "=============="
#for row in data:
#    print row

data = numpy.loadtxt(filename,dtype="string",delimiter = ",")
print type(data)
print data