import numpy as np
#1
numpy_array = np.arange(10)
print(numpy_array)
print('kieu du lieu:',numpy_array.dtype)
print('do dai arr:',len(numpy_array))
print('do dai arr:',numpy_array.size)
#2
arr_odd = numpy_array[1::2]
arr_even = numpy_array[0::2]
arr_odd = numpy_array[numpy_array%2==1]
arr_even = numpy_array[numpy_array%2==0]
print(arr_odd)
print(arr_even)
#3
arr_update_1 = []
for i in numpy_array:
    if i in arr_odd:
        i = 100
    arr_update_1.append(i)
arr_update_1 = np.array(arr_update_1)
print(arr_update_1)