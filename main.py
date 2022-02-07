from functions import transform, axis_rotation, custom_axis_rotation
import numpy as np

print(axis_rotation(60, 'x'))
print(axis_rotation(60, 'y'))
print(axis_rotation(60, 'z'))

print (custom_axis_rotation(60, np.array([5, 25, 35])))

print(transform(60, 'x', np.array([5, 25, 35])))
print(transform(60, np.array([5, 5, 5]), np.array([5, 25, 35])))