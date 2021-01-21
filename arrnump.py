import numpy as np

array_two = np.arange(1,4)**2
# print(array_two)

array_three = np.arange(1,4)**3
print("sum is",array_two+array_three)

#let's print power using np.array

print("using array with np.power",np.power(np.array([1,2,3]),4))

print("this is negetive array",np.negative(np.array([1,2,3])))

sample_array = np.array([1,2,3])

print("This is exponential value of the array",np.exp(sample_array))

print("this is log",np.log(sample_array))

print("This is sin",np.sin(sample_array))
