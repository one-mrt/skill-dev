import numpy as np
from IPython.display import display
from numpy.lib.function_base import disp

a = np.array([1,4,5,8], float)

print(a)
print(type(a))

a = np.array([[1,2,3],[4,5,6],[7,-2,9]],float)
display(a)
display(a[0][2])
display(a.shape)
display(a.dtype)
print(len(a))
disp(a.dtype)
disp(-2 in a)


b = np.array(range(12),float)
b = b.reshape((4,3))

disp(b)


c = np.array(range(12),float).reshape((4,3))
disp(c)
disp('===')
disp(c.transpose())