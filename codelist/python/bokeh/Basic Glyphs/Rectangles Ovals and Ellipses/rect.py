#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for boken"

from math import pi
from bokeh.plotting import output_file,figure,show

output_file("Rectangles, Ovals and Ellipses.html")

p = figure(width = 600,height = 600)

p.quad(top = [2,6,9],bottom = [1,5,8],left = [1,2,3],right = [3,4,5],color = ['navy','blue','red'],alpha = 0.5)

p.rect([1,2,3],[1,2,3],width = 0.8,height = 1.2,angle = pi/3)

p.oval([1,2,3],[3,4,5],width = 0.8,height = 2.8,angle = pi/3,color = "green")

p.ray(x=[1, 2, 3], y=[1, 2, 3], length=45, angle=[30, 45, 60],
      angle_units="deg", color="#FB8072", line_width=2)

show(p)