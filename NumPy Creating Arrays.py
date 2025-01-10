# Dimensions in Arrays

# 0-D Arrays

import numpy as np
arr = np.array(42)
print(arr)

# 1-D Arrays

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# 2-D Arrays

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# 3-D arrays

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


# Check Number of Dimensions?

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Higher Dimensional Arrays

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

