import numpy as np
mat_a=np.matrix([0,3,5,5,5,2]).reshape(2,3)
print("reshaped mat_a\n",mat_a)

mat_b=np.matrix([3,4,3,-2,4,-2]).reshape(3,2)
print("reshaped mat_b\n",mat_b)

mat_c=mat_a*mat_b
print('multiplication of a and b',mat_c)
