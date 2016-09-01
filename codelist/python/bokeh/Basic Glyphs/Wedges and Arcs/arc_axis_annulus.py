#/user/bin/env python   

# -*- coding:utf-8 -*-

"this is a test module for boken"

from bokeh.plotting import figure,show,output_file
from bokeh.models import Range1d

output_file("arc.html")
p = figure(width = 400,height = 400,x_axis_type="datetime")
#p = figure(width = 400,height = 400,x_range = ["a", "b", "c", "d", "e", "f", "g", "h"])
# set a range using a Range1d
#p.x_range = Range1d(0, 6)
#p.x_range = ["a", "b", "c", "d", "e", "f", "g", "h"] #类型不对
p.y_range = Range1d(0, 6)

p.arc(x=[1,2,3],y=[1,2,3],radius = 0.1,start_angle = 0.4,end_angle = 4.8)
p.annular_wedge(x=[1, 2, 3], y=[2, 3, 4], inner_radius=0.1, outer_radius=0.25,
                start_angle=0.4, end_angle=4.8, color="green", alpha=0.6)
p.wedge(x=[1,2,3],y=[3,4,5],radius = 0.1,start_angle = 0.4,end_angle = 4.8,color = 'firebrick',alpha = 0.5)

p.annulus(x=[1, 2, 3], y=[4, 5, 6], inner_radius=0.1, outer_radius=0.25,
          color="orange", alpha=0.6)
show(p)