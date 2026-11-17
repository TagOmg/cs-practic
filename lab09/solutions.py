import numpy as np

def make_hour():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    return dict(third = values[2], last = values[-1] , middle = values[2:6], every_second = values[::2], reversed = values[::-1])

def change_vector(values):
    new_values = np.asarray(values).copy()
    new_values[2:4] = 99
    new_values[::2] = -1
    return new_values.tolist()

def cap_above(values,limit):
    values = np.asarray(values)
    values[values > limit] = limit
    return values.tolist()

def celsius_to_fahrenheit(values):
    values = np.asarray(values)
    values[:] = values[:] * 9 / 5 + 32
    return values.tolist()
print(vector_report([0, 3, 6, 9, 12, 15, 18, 21]))