import matplotlib.pyplot as plt
import numpy as np

size = 1

csv_data = np.genfromtxt('firebase/4/4_165.csv', delimiter=',')
# csv_data = np.genfromtxt('drivers/156/100.csv', delimiter=',')
csv_data = csv_data[1:]

t_csv_data = np.array(csv_data).T
xmin = min(t_csv_data[0])
xmax = max(t_csv_data[0])
ymin = min(t_csv_data[1])
ymax = max(t_csv_data[1])

x_zero = csv_data[0][0]
y_zero = csv_data[0][1]
x_max = x_zero + xmax
y_max = y_zero + ymax
x_min = x_zero - xmax
y_min = y_zero - ymax

# print("xmin xmax: {}, {}".format(xmin, xmax))
# print("ymin ymax: {}, {}".format(ymin, ymax))

final_data = csv_data
for i in final_data:
    i[0] = (i[0]-x_zero) / (xmax-x_min)
    i[1] = (i[1]-y_zero) / (ymax-y_min)
    # i[0] = (i[0]-x_min) / (x_max-x_min) * 10000000000000000000000.0
    # i[1] = (i[1]-y_min) / (y_max-y_min) * 10000000000000000000000.0

data = np.array(final_data).T

Xmin = min(data[0])
Xmax = max(data[0])
Ymin = min(data[1])
Ymax = max(data[1])

print(data)

print("xmin xmax: {}, {}".format(Xmin, Xmax))
print("ymin ymax: {}, {}".format(Ymin, Ymax))

fig = plt.figure()
ax = fig.add_subplot(size, size, size)

# ax.set_xlim([x_min, x_max])
# ax.set_ylim([y_min, y_max])
# tick_list = [i for i in range(0,101, 1)]
# ax.set_xticks(tick_list)
# ax.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])

# even_list = [2*i for i in range(len(data[0])//2)]
# even_list2 = [2*i for i in range(len(data[1])//2)]
even_list = [24*i for i in range(len(data[0])//24)]
even_list2 = [24*i for i in range(len(data[1])//24)]

print(len(data[0]), len(data[1]))
print(len(even_list), len(even_list2))

ax.plot(data[0][:], data[1][:], label='Label_1')
ax.plot(data[0][even_list], data[1][even_list2], label='Label_2')
plt.legend(['Origin', '24-step'])

plt.xlabel('latitude')
plt.ylabel('longitude')
plt.show()