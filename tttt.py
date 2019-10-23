import numpy as np


# a1 = np.array([[1,2,3,4,5], [6,7,8,9,0]])
a1 = np.array([1,2,3,4,5])
print(a1.shape)
print(a1)

a2 = np.roll(a1, 1, axis=0)
print(a2)




#############################################################
# a1 = np.array([1., 2., 3., 4., 5.]).reshape(-1, 1)
# a2 = np.array([6., 7., 8., 9., 0.]).reshape(-1, 1)

# result = np.hstack([a1, a2])

# print(result, result.shape)

# np.savetxt('output.csv', result, delimiter=",")
#############################################################
# f = open('output.csv', 'w')
# csv_writer = csv.writer(f)
# csv_writer.writerow(result)
# f.close()

# a2 = np.array([6, 7, 8, 9, 0])



# print(np.vstack([a1, a2]))

# a1 = np.transpose(a1)
# a2 = np.transpose(a2)

# print(np.vstack([a1, a2]))

# f = open('output.csv', 'w')
# csv_writer = csv.writer(f)
# csv_writer.writerow(np.vstack([a1, a2]))
# f.close()