import numpy as np

myList = [[1,2], [2,3], [3,4], [4,5]]

np.savetxt('output.csv', myList, delimiter=',', fmt='%1.2f')