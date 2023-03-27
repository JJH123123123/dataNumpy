import numpy as np 

# print(dir(np))

print(np.pi)




arr = np.array([1,2,3])
print(arr)

print(type(arr))


arr2d = np.array([[1,2,3,], [4,5,6]])
print(arr2d)

print(arr2d.ndim)
print(arr2d.shape)

print(arr[0])


print(arr2d[0])

print(arr2d.dtype)


list_2d = [[1.1, 2.1, 4.3], [7.3, 10.2, 9.1]]
arr2d_1 = np.array(list_2d)

print(arr2d_1)
print(type(arr2d_1.dtype))
print(type(arr2d_1))
print(arr2d_1.shape)

# concatenate 
arr_concat = np.concatenate([arr2d_1, arr2d])
print(arr_concat, type(arr_concat))
# arr_vstack = np.vstack((arr2d. arr2d_1))
# print(arr_vstack)


