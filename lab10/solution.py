import numpy as np

def make_table(rows,columns):
    return np.arange(rows*columns).reshape(rows,columns)



def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    new = matrix.copy
    new[row_start:row_stop,column_start:column_stop] = value
    return  new



def matrix_vector_product(matrix, vector):
    return matrix @ vector


def matrix_multiply(left, right):
    return left @ right

def transpose_matrix(matrix):
    return matrix.T

def solve_system(matrix, vector):
    return np.linalg.solve(matrix,vector)


def tensor_channel_mean(tensor):
    return np.mean(tensor, axis=-1)

def point_distance(first, second):
    return np.linalg.norm(first,second)