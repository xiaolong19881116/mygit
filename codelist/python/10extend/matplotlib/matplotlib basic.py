'''
figure��������
axis��������ָ�����ᣬ��ָҪ����ͼ�Ρ�
xlabel��ylabel���������������
�̶�
ͼ��
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
���ͼ�λ���һ�Ż�����
'''
fig, ax = plt.subplots()
# ��label��д��ѧ��ʽ
ax.plot(x,y3,color = "blue",label = r"$y(6x+10$)")
ax.plot(x,y,color = "red",label = "$y(x)$")
# ��x�ᡢy�ᣬȥ���ı�
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

# ��ʾy��������ޣ�����40�����ޣ�15��
ax.set_ylim(-15, 40)
# ��y��Ŀ̶Ⱥ�x��Ŀ̶�
ax.set_yticks([-10, 0, 10, 20, 30])
ax.set_xticks([-4, -3, -2, -1, 0, 1, 2])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# ��ʾx���y����Ե�label
ax.set_xlabel("$x$", fontsize=18)
ax.set_ylabel("$y$", fontsize=18)
# ��ʾͼ��λ�ã�0��ʾ��ѣ�best��ncol��ʾͼ��Ҫ�ּ��С�frameon��ʾ�Ƿ���Ҫͼ�������
ax.legend(loc=0, ncol=3, fontsize=14, frameon=False);
#fig.savefig("figure-1.pdf")