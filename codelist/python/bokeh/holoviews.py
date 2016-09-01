import numpy as np
import holoviews as hv 
hv.notebook_extension("bokeh")
xs = np.linspace(0,np.pi*4,100)
data = (xs,np.sin(xs))
hv.Curve(data)