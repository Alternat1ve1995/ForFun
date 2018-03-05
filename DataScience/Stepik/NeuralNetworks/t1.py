import numpy as np
import matplotlib as mp

mat = np.eye(3, 4, 1)+2*np.eye(3, 4, 0)

print(mat.reshape(mat.size, 1))
