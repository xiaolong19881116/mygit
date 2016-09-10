'''
figure：即画布
axis：本义是指坐标轴，借指要画的图形。
xlabel、ylabel：横坐标和纵坐标
刻度
图例
'''

%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,2,100)
y = x
y1 = x**3 + 5*x**2 +10
y2 = 3*x**2 + 10*x 
y3 = 6*x + 10
#plt.plot(x,y)
#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(x,y3)
#plt.scatter(x, y1)

'''
多个图形画在一张画布上
'''
fig, ax = plt.subplots()
# 给label书写数学公式
ax.plot(x,y3,color = "blue",label = r"$y(6x+10$)")
ax.plot(x,y,color = "red",label = "$y(x)$")
# 画x轴、y轴，去掉四边
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

# 显示y轴的上下限（上限40，下限－15）
ax.set_ylim(-15, 40)
# 画y轴的刻度和x轴的刻度
ax.set_yticks([-10, 0, 10, 20, 30])
ax.set_xticks([-4, -3, -2, -1, 0, 1, 2])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 显示x轴和y轴各自的label
ax.set_xlabel("$x$", fontsize=18)
ax.set_ylabel("$y$", fontsize=18)
# 显示图例位置，0表示最佳，best。ncol表示图例要分几列。frameon表示是否需要图例的外框。
ax.legend(loc=0, ncol=3, fontsize=14, frameon=False);
#fig.savefig("figure-1.pdf")