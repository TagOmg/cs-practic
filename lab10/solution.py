import numpy as np

def make_table(rows,columns):
    return np.arange(rows*columns).reshape(rows,columns).tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    matrix = np.array(matrix)

    return matrix[row_start:row_stop,column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    new = np.array(matrix).copy()
    new[row_start:row_stop,column_start:column_stop] = value
    return  new.tolist()



def matrix_vector_product(matrix, vector):
    matrix = np.array(matrix)
    vector = np.array(vector)

    return (matrix @ vector).tolist()


def matrix_multiply(left, right):
    left = np.array(left)
    right = np.array(right)

    return (left @ right).tolist()

def transpose_matrix(matrix):
    matrix = np.array(matrix)

    return matrix.T.tolist()

def solve_system(matrix, vector):
    matrix = np.array(matrix)
    vector = np.array(vector)

    return np.linalg.solve(matrix,vector).tolist()


def tensor_channel_mean(tensor):
    tensor = np.array(tensor)

    return np.mean(tensor, axis=-1).tolist()


def point_distance(first, second):
    first = np.array(first)
    second = np.array(second)

    return np.linalg.norm(first,second).tolist()