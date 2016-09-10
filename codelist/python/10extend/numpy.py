import numpy as np
s = np.array([1,2,3,4,5])
s2 = np.linspace(1,100,100)
s3 = s2 > 50
s3[0:60]
arr = np.arange(10)

arr2 = arr.reshape(2,5)

print arr
print arr2

print arr.dtype
print arr2.dtype

print arr.size
print arr2.size

print arr.ndim
print arr2.ndim

print arr.shape
print arr2.shape

print arr.nbytes
print arr2.nbytes

print arr.min()
print arr2.min()

print arr.max()
print arr2.max()

print arr.sum()
print arr2.sum()

print arr.prod()
print arr2.prod()

print arr.mean()
print arr2.mean()

print arr.std()
print arr2.std()

print "######################################################"

arr1 = np.arange(4)
arr2 = np.arange(10, 14)
print arr1
print arr2
print arr1 + 100
print arr1 + arr2
print arr1 - arr2
print arr1 * arr2
print arr1 / arr2

print "######################################################"

v1 = np.array([2,3,4])
v2 = np.array([1,1,1])
print v1
print v2
print np.dot(v1,v2)

v3 = np.arange(6).reshape(2,3)
print v3
print np.dot(v3,v1)

#Text mode
arr = np.arange(10).reshape(2,5)
np.savetxt('text.out', arr, fmt='%2d', header='My data set')

arr2 = np.loadtxt('text.out')
print arr2

print np.random.uniform(10,20,20)
print np.random.randn(10)
print np.random.randint(10,50,100)

x=['Python','data','random','Mining','good']
np.random.shuffle(x)
print x