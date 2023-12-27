import numpy as np
arr_a =np.array ([1,2,3,2,3,4,3,4,5,6])
arr_b =np.array ([7,2,10,2,7,4,9,4,9,8])
#1
a=[i for i in arr_a if i in arr_b]
arr_c = np.array(a)
print(arr_c)
#2
arr_d = np.array(list(set(arr_a)- set(arr_b)))
print(arr_d)
#3
arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = np.array([i for i in arr_e if i>=5 and i<=10])
print(arr_f)