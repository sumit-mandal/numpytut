import numpy as np

x=np.arange(9).reshape(3,3)
print(x)

ravelled_array = x.ravel()
print(f"This is used for converting multidimesional-array to single array\n {ravelled_array}")


flattend_array=x.flatten()
print(f"This is flatten array\n{flattend_array}")
#flatten makes the copy of array and gives output.It doesn't makes changes in original array
#ravel returns views of the original array

y=np.arange(2,11)
y.shape=[3,3]
print(y.transpose())

#if value is not big enough 'resize' repeats the value in array
print("resized array",np.resize(y,(6,6)))

print("Using np.zero",np.zeros((2,3),dtype=int))
print("Using np.ones",np.ones((6),dtype=int))

print("using np.eye",np.eye(4))

print("Random array between o-1",np.random.rand(2,3))
