import numpy as np

x=np.arange(18).reshape(3,2,3)
print(x)

k=x[2,0,0:3]
print('sliced array',k)

comparison_operation = x>5
print(comparison_operation)
print(x[comparison_operation])
