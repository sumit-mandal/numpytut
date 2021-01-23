import numpy as np

x=np.arange(6).reshape(2,3)
print("a is",x)

y=np.arange(6,14).reshape(2,4)
print("b is",y)

z=np.hstack((x,y))
print("Merging x and y\n",z)

#hstack means horizontal stack
#vstack means vertical stack

#in hstack array should be vertically smae for all the arrays.i.e. number of rows should be same
#in vstack array should be horizontally same.i.e. number of columns should be same

k = np.arange(10,16).reshape(2,3)
print("value of k is\n",k)

l = np.arange(20,35).reshape(5,3)
print("value of l is\n",l)

m = np.vstack((k,l))
print("merging k and l\n",m)

#depthstack is used for aligning array diagonally

a=np.arange(4).reshape(2,2)
b=np.arange(4,8).reshape(2,2)

depth_stack=np.dstack((a,b))
print("this is dstack\n",depth_stack)
