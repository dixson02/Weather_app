import numpy as np
import time
size=1000000
array1 = np.arange(size)
array2 = np.arange(size)

start_time = time.time()
result = array1 + array2
end_time = time.time()

print("NumPy arrays time:", end_time - start_time)
