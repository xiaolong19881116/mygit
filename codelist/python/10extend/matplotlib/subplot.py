fig, axes = plt.subplots(1,2,figsize=(8,3.5), sharey=True) # sharey表示两个图共享一个y轴
data1 = np.random.randn(200,2)*np.array([3,1]) # 第一列扩大3倍
data2 = np.random.randn(200,2)*np.array([1,3]) # 第二列扩大3倍
axes[0].scatter(data1[:,0], data1[:,1], color="green", marker="s", s=30, alpha=0.5) # alpha表示透明度
axes[0].scatter(data2[:,0], data2[:,1], color="blue", marker="o", s=30, alpha=0.5)
axes[1].hist([data1[:,1], data2[:,1]], bins=15, color=["green","blue"], alpha=0.5, orientation="horizontal"); # 如果不加分号会把array的值输出。