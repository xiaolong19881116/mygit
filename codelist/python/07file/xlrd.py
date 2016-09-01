#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for xlrd"

import xlrd 
import types

meta = xlrd.open_workbook("abc.xlsx")
table = meta.sheets()[0]

nrows = table.nrows
ncols = table.ncols 

print nrows,ncols

def checkInt(number):
    if (type(number) == types.IntType or type(number) == types.FloatType) and number % 1 == 0:
        return int(number)
    else:
        return number

def format_list(li):
    return u"| " + u"| ".join([unicode(x) for x in li]) + u" |\n"

col_name = []
for n in range(ncols):
    col_name.append(table.cell(0,n).value)

f = open("output.txt","w")

f.write(format_list(col_name).encode('utf-8'))
f.write(format_list([u":--------: "] * ncols).encode('utf-8'))

row_data = []
rowstr = ""
for r in range(1,nrows):
    for n in range(ncols):
        row_data.append(unicode(checkInt(table.cell(r,n).value)))
    f.write(format_list(row_data).encode('utf-8'))
    row_data = []
f.close()

print "done"