#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for boken"

#导入
from bokeh.plotting import figure,output_file,show

#准备数据
x = [1,2,3,4,5]
y = [2,5,3,6,4]

#创建输出文件
output_file("test_line.html")

#创建图例
p = figure(title = "Simple line",x_axis_label = "x",y_axis_label = "y")
p.line(x,y,legend = "Temp")
p.multi_line([[1,3,2],[3,4,6,6]],[[2,1,4],[4,7,8,5]],color = ["firebrick","navy"],alpha=[0.8,0.3],line_width = 3)

#显示图例：
show(p)