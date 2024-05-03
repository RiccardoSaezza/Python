import numpy as np

array = np.empty((2, 3))

print("primo array: ")
print(array)

array2 = np.reshape(array, (3, 2, 1))

print("secondo array: ")
print(array2)

array[0][1] = 1
print("Aggiunta di un valore")
print(array)

