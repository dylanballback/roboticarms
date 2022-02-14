from sre_compile import isstring
from turtle import back

import numpy as np
import math

def axis_rotation(angle, axis):
    """
    Takes in an angle in degrees and a axis to rotate around and returns rotation matrix.

        Parameters:
                angle (float): Angle of rotation
                axis (str): Axis of rotation ('x','y', or 'z') 

        Returns:
                Rotation matrix of angle about axis of rotation entered
    """
    
    #convert angle from degrees to radians
    angle_rad = math.radians(angle)
    
    #Define s as sin(angle in radians)
    s = np.sin(angle_rad)
    #Define c as sin(angle in radians)
    c = np.cos(angle_rad)


    if axis == 'x':
        Rx = np.array([(1, 0, 0),
                       (0, c, -s),
                       (0, s, c)], dtype=float)
        return (Rx)
    elif axis == 'y':
        Ry = np.array([(c, 0, s),
                       (0, 1, 0),
                       (-s, 0, c)], dtype=float)
        return (Ry)
    elif axis == 'z':
        Rx = np.array([(c, -s, 0),
                       (s, c, 0),
                       (0, 0, 1)], dtype=float)
        return (Rx)
    else:
        print("Error")



def custom_axis_rotation(angle, axis_vector):
    """
    Takes in an angle in degrees and a custom axis vector to rotate around and returns rotation matrix.

        Parameters:
                angle (float): Angle of rotation
                axis_vector (np.array): Custom Axis of rotation vector array ([0, 0, 0]) 

        Returns:
                Rotation matrix of angle about custom axis vector of rotation entered
    """

    #convert angle from degrees to radians
    angle_rad = math.radians(angle)
    
    #Define s as sin(angle in radians)
    s = np.sin(angle_rad)
    #Define c as cos(angle in radians)
    c = np.cos(angle_rad)

    #Normalizes the axis vector
    axis_vector_norm = axis_vector / np.linalg.norm(axis_vector)

    v = 1 - c
   
   #Define x, y, z of normalized vector
    x = axis_vector_norm[0]
    y = axis_vector_norm[1]
    z = axis_vector_norm[2]
  
    #Break down of custom axis rotation matrix calculations
    aa = x*x*v+c
    ab = x*y*v-z*s
    ac = x*z*v+y*s
    
    ba = x*y*v+z*s
    bb = y*y*v+c
    bc = y*z*v-x*s

    ca = x*z*v-y*s
    cb = y*z*v+x*s
    cc = z*z*v+c

    custom_axis_rotation_matrix = np.array([(aa, ab, ac),
                                            (ba, bb, bc),
                                            (ca, cb, cc)], dtype=float)

    return custom_axis_rotation_matrix


def custom_transform(angle, axis, pos):
    """
    Takes in an angle in degrees and rotation axis of the base frame or custom axis vector to rotate around
    and the subsequent 1x3 translation vector  and returns the transform rotation matrix.
        Parameters:
                angle (float): Angle of rotation
                axis (np.array or str): Custom Axis of rotation vector array ([0, 0, 0]) or str for axis of rotation ('x','y', or 'z')
                pos (np.array): Translation vector in a 1x3 matrix
        Returns:
                Rotation transform matrix of a angle about rotation axis of the base frame or custom axis vector of rotation by the custom translation vector entered
    """
    #Check if axis is a string
    if isstring(axis) == 1:
        #Check if axis is rotation about axis x, y, or z
        if axis == 'x' or axis == 'y' or axis == 'z':
            r_m = axis_rotation(angle, axis)
    elif axis.size == 3:
        r_m = custom_axis_rotation(angle, axis)
    
    t_v = pos

    transform_matrix = np.array([(r_m[0,0], r_m[0,1], r_m[0,2], t_v[0]),
                                 (r_m[1,0], r_m[1,1], r_m[1,2], t_v[1]),
                                 (r_m[2,0], r_m[2,1], r_m[2,2], t_v[2]),
                                 (0, 0, 0, 1)], dtype=float)
    return transform_matrix




def link_transform(alpha, a, d, theta):

    #convert angle theta from degrees to radians
    angle_t_rad = math.radians(theta)
    #convert angle alpha from degrees to radians
    angle_a_rad = math.radians(alpha)
    
    #Define s_t as sin of theta (angle in radians)
    s_t = np.sin(angle_t_rad)
    #Define c_t as cos of theta (angle in radians)
    c_t = np.cos(angle_t_rad)

    #Define s_a as sin of alpha (angle in radians)
    s_a = np.sin(angle_a_rad)
    #Define c_a as cos of alpha (angle in radians)
    c_a = np.cos(angle_a_rad)


    #Define Matrix variable calulations 
    aa = c_t
    ab = -s_t
    ac = 0
    ad = a

    ba = s_t*c_a
    bb = c_t*c_a
    bc = -s_a
    bd = -s_a*d

    ca = s_t*s_a
    cb = c_t*s_a
    cc = c_a
    cd = c_a*d

    da = 0
    db = 0
    dc = 0
    dd = 1

    link_t_matrix = np.array([(aa, ab, ac, ad),
                              (ba, bb, bc, bd),
                              (ca, cb, cc, cd),
                              (da, db, dc, dd)])
    return link_t_matrix
