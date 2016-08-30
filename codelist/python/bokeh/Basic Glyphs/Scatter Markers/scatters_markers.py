#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for boken"

#导入
from bokeh.plotting import figure,output_file,show

#准备数据
x = [1,2,3,4,5]
y0 = [1,2,3,4,5]
y1 = [2,3,4,5,6]
y2 = [3,4,5,6,7]
y3 = [4,5,6,7,8]
y4 = [5,6,7,8,9]
y5 = [6,7,8,9,10]
y6 = [7,8,9,10,11]
y7 = [8,9,10,11,12]
#创建输出文件
output_file("scatters.html")

#创建图例
p = figure(title = "scatters",x_axis_label = "x",y_axis_label = "y")
p.circle(x,y0,size = 10,color = "navy",alpha = 0.5)
p.square(x,y1,size = 10,color = "olive",alpha = 0.5)
p.cross(x,y2,size = 10,color = "red",alpha = 0.5)
p.diamond(x,y3,size = 10,color = "green",alpha = 0.5)
p.asterisk(x,y4,size = 10,color = "blue",alpha = 0.5)
p.x(x,y5,size = 10,color = "red",alpha = 0.5)
p.triangle(x,y6,size = 10,color = "green",alpha = 0.5)
p.circle_cross(x,y7,size = 10,color = "red",alpha = 0.3)

#显示图例：
show(p)