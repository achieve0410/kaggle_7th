import math
import numpy as np

import settings

def build_features4(ride, index, step=3, version=1):
  MIN_DIST_TH = 7 if version == 1 else 0.2
  ride2 = np.array(ride)
  ride1 = np.roll(ride2, step, axis=0)
  ride0 = np.roll(ride1, step, axis=0)

  ride0 = ride0[step*2:]
  ride1 = ride1[step*2:]
  ride2 = ride2[step*2:]

  a1 = np.array(ride1 - ride0)
  a2 = np.array(ride2 - ride1)

  distances1 = np.linalg.norm(a1, axis=1)
  distances2 = np.linalg.norm(a2, axis=1)
  distances = (distances1 + distances2)
  accel = distances2 - distances1

  distances3 = np.linalg.norm(a1, axis=1).reshape(-1, 1)
  distances4 = np.linalg.norm(a2, axis=1).reshape(-1, 1)
  distance = (distances3 + distances4)
  accels = distances3 - distances4

  result = np.hstack([distance, accels])
  # np.savetxt('result/output'+str(index)+'.csv', result, delimiter=',', fmt='%1.2f')

  np.seterr(all='ignore')
  angles = np.arccos((a1 * a2).sum(1) / (distances1 * distances2))

  np.seterr(all='print')
  angles[distances1 < MIN_DIST_TH] = 0
  angles[distances2 < MIN_DIST_TH] = 0
  angles = angles * 180 / math.pi

  if version == 1:
    DIST_THR = np.array([1, 11, 16, 26, 36, 56, 80]) * step
  else:
    DIST_THR = np.array([1, 11, 25, 45, 70]) * step
  distances = np.digitize(distances, DIST_THR)
  ANGL_THR = np.array([10, 30, 60, 100])
  angles = np.digitize(angles, ANGL_THR)
  ACCEL_THR = np.array([-3, -1.5, -0.3, 0.3, 1.5, 3]) * step
  accel = np.digitize(accel, ACCEL_THR)

  print("distances : {}, angles : {}, accel: {}".format(distances, angles, accel))

  movements = np.vstack((distances, angles, accel)).transpose()
  movement_string = ' '.join(['%s_%s_%s' % (m[0], m[1], m[2]) for m in movements])
  # print(movement_string)

  return movement_string
