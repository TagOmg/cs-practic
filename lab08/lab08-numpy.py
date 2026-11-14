import numpy as np
#1 задание
print('Задание 1')

hours = np.arange(0,22,3)
line = np.linspace(0,1,num=5)
zeros = np.zeros(5, dtype=int)
unknow_table = np.full((2,3),-1)
identity = np.ones((3,3), dtype = int)

print(hours,hours.shape,hours.ndim,hours.size,hours.dtype)

#2 задание
print('\nЗадание 2')
print('\n',hours[2],hours[-1],hours[2:5],hours[::2])
print(hours[::-1])




#3 задание
print('\nЗадание 3')

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\n",temperatures.shape, temperatures.ndim, temperatures.size)

print(temperatures[1][2], temperatures[:,-1])
print(temperatures[:2,1:])
print(temperatures[:2,1:3])
print(temperatures[:,1:3])

#Задание 4
print('\nЗадание 4\n')

matrix = np.arange(1,26).reshape(5,5)
print(matrix[:3])
print(matrix[:3].shape)
print(matrix[3:])
print(matrix[3:].shape)
print(matrix[:,:2])
print(matrix[:,:2].shape)
print(matrix[:3,1:4])
print(matrix[:3,1:4].shape)
print(matrix[-2:,-2:])
print(matrix[-2:,-2:].shape)

#Задание 5
print("\nЗадание 5\n")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
changed_hours = hours.copy()
changed_hours[1:4]=99
print(changed_hours)
print(hours)
changed_matrix = matrix.copy()
changed_matrix[2]= 0
changed_matrix[:,-1] = -1
changed_matrix[1:4,1:4] = 100
print(changed_matrix)
print(matrix)

#Задание 6
print('\nЗадание 6\n')
numbers = np.arange(0,12)
table = numbers.reshape(3,4)
transposed = numbers.T
print(numbers)
print(table)
print(transposed)