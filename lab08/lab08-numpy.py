import numpy as np
#1 задание
hours = np.arange(0,22,3)
line = np.linspace(0,1,num=5)
zeros = np.zeros(5, dtype=int)
unknow_table = np.full((2,3),-1)
identity = np.ones((3,3), dtype = int)

print(hours,hours.shape,hours.ndim,hours.size,hours.dtype)

#2 задание
print('\n',hours[2],hours[-1],hours[2:5],hours[::2],hours[::-1])




#3 задание
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\n",temperatures.shape, temperatures.ndim, temperatures.size)
print(temperatures[1][2], temperatures[:,-1],temperatures[:2,1:])