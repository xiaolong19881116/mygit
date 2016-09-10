%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

s = pd.Series([909976, 8615246, 2872086, 2273305])
print s 
print s.describe()

pd.set_option('display.mpl_style', 'default')


fig, axes = plt.subplots(1,4, figsize=(12,3))

s.plot(kind="line", ax=axes[0], title="line") 
s.plot(ax=axes[1], kind='bar', title='bar')
s.plot(ax=axes[2], kind='box', title='box')
s.plot(ax=axes[3], kind='pie', title='pie')

fig.tight_layout()
fig.savefig("ch4-series-plot.pdf")
fig.savefig("ch4-series-plot.png")