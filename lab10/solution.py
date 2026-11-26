import numpy as np

def make_table(rows,columns):
    return np.arange(rows*columns).reshape(rows,columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    return matrix[row_start:row_stop,column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    new = matrix.copy()
    new[row_start:row_stop,column_start:column_stop] = value
    return  new.tolist()



def matrix_vector_product(matrix, vector):
    return (matrix @ vector).tolist()


def matrix_multiply(left, right):
    return (left @ right).tolist()

def transpose_matrix(matrix):
    return matrix.T.tolist()

def solve_system(matrix, vector):
    return np.linalg.solve(matrix,vector).tolist()


def tensor_channel_mean(tensor):
    return np.mean(tensor, axis=-1).tolist()


def point_distance(first, second):
    return np.linalg.norm(first,second).tolist()