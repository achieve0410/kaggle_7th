import matplotlib.pyplot as plt
import numpy as np

size = 1

csv_data = np.genfromtxt('firebase/4/4_132.csv', delimiter=',')
# csv_data = np.genfromtxt('drivers/1/100.csv', delimiter=',')
csv_data = csv_data[1:]

t_csv_data = np.array(csv_data).T
xmin = min(t_csv_data[0])
xmax = max(t_csv_data[0])
ymin = min(t_csv_data[1])
ymax = max(t_csv_data[1])

x_zero = csv_data[0][0]
y_zero = csv_data[0][1]

# print("xmin xmax: {}, {}".format(xmin, xmax))
# print("ymin ymax: {}, {}".format(ymin, ymax))

final_data = csv_data
for i in final_data:
    # i[0] = (i[0]-xmin) / (xmax-xmin)
    # i[1] = (i[1]-ymin) / (ymax-ymin)
    i[0] = (i[0]-x_zero) / (xmax-xmin) * 10000
    i[1] = (i[1]-y_zero) / (ymax-ymin) * 10000

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

ax.set_xlim([Xmin, Xmax])
ax.set_ylim([Ymin, Ymax])
tick_list = [i for i in range(0,10001, 1)]
ax.set_xticks(tick_list)
ax.set_yticks(tick_list)

ax.plot(data[0][20:30], data[1][20:30])

plt.xlabel('latitude')
plt.ylabel('longitude')
plt.show()