import os
import os.path
import random

import util
import settings_2
from datetime import datetime

class DataAccess:
 
  def get_drivers(self):
    return settings_2.DRIVER_IDS

  def get_ride(self, driver_id, ride_id):
    filename = '%s/%s/logfile%s.txt' % (settings_2.DATA_FOLDER, driver_id, ride_id)
    # print("filename : {}".format(filename))
    data = open(filename, 'r').readlines()
    d = []
    for i in data:
          dat = i[46:53]
          d.append(float(dat))
    return d

  def get_rides(self, driver_id):
    for ride_id in range(1, 11, 1):
      yield self.get_ride(driver_id, ride_id)

  def get_rides_2(self, driver_id, size):
    seed = random.Random(x=datetime.now())
    rides = set([i for i in seed.sample(10, size)])
    for ride_id in rides:
      yield self.get_ride(driver_id, ride_id)

  def get_ride_segments(self, driver_id, ride_id, version=1):
    filename = '%s/%s_%s.csv' % (settings_2.SEGMENTS_FOLDER[version], driver_id, ride_id)
    data = open(filename, 'r').read()
    data = [[int(x) for x in row.split(',')] if row else [] for row in data.split('\n')]
    if data == [[]]:
      print (driver_id)
      print (ride_id)
    return data

  def get_rides_segments(self, driver_id, version=1):
    for ride_id in range(1, 201):
      yield self.get_ride_segments(driver_id, ride_id, version=version)

  def write_ride_segments(self, driver_id, ride_id, lengths, times, angles, version=1):
    filename = '%s/%s_%s.csv' % (settings_2.SEGMENTS_FOLDER[version], driver_id, ride_id)
    f = open(filename, 'w')
    f.write('%s\n' % util.get_list_string(lengths))
    f.write('%s\n' % util.get_list_string(times))
    f.write('%s' % util.get_list_string(angles))
    f.close()

  def skip_segment(self, driver_id, ride_id, version=1):
    filename = '%s/%s_%s.csv' % (settings_2.SEGMENTS_FOLDER[version], driver_id, ride_id)
    return os.path.isfile(filename)

  def get_random_drivers(self, size, seed, exception):
    # old version for small samples (without replacement)
    if size <= 2000:
      sample = [settings_2.DRIVER_IDS[i] for i in seed.sample(range(len(settings_2.DRIVER_IDS)), size+1)]
      if exception in sample:
        sample.remove(exception)
      else:
        sample = sample[:-1]
      return sample

    # new version - large numbers, with replacement
    sample = []
    while len(sample) < size:
      new = settings_2.DRIVER_IDS[seed.randint(0, len(settings_2.DRIVER_IDS) - 1)]
      if new != exception:
        sample.append(new)
    return sample

  def get_rides_split(self, driver_id, size_train, segments=False, version=1):
    seed = random.Random(x=driver_id)
    if not segments:
      rides = list(self.get_rides(driver_id)) ## rides[0] = gps of 842 row data, rides[1] = gps of 958 row data, ...
      # print(len(rides[0]))
    else:
      rides = list(self.get_rides_segments(driver_id, version=version))

    split_train = set([i for i in seed.sample(range(200), size_train)])
    ## split 200 trips
    rides_train = [rides[i] for i in split_train] ## len(rides_train) = 180
    rides_test = [rides[i] for i in range(200) if i not in split_train] ## len(rides_test) = 20
    # print("rides_train: {}\n rides_test: {}\n".format(rides_train, rides_test))
    return rides_train, rides_test

  def get_rides_train(self, driver_ids, size_train, segments=False, version=1):
    seed = random.Random(x=datetime.now())
    X = []
    Y = []

    for driver in driver_ids:
      rides = list(self.get_rides(driver)) ## rides[0] = gps of 842 row data, rides[1] = gps of 958 row data, ...
      print(len(rides))

      # print(driver, len(rides))
      # print(settings_2.RIDE_IDS[driver])

      train_x = [rides[i] for i in range(10)] ## len(train_x) = 200
      train_y = [driver for i in range(10)] ## len(train_y) = 200
      print("driver_id: {}\ntrain_x: {}\n train_y: {}\n".format(driver, len(train_x), train_y))
      X.extend(train_x)
      Y.extend(train_y)

    return X, Y

  def get_rides_test(self, driver_ids, size_test, segments=False, version=1):
    # tripList = [1,50, 70, 144, 800, 1400, 1553, 2106, 2653, 3159, 3300]
    # driver_id = driver_ids[tripList]
    # split_train = set([i for i in seed.sample(range(200), size_train)])
    seed = random.Random(x=datetime.now())
    X = []
    Y = []

    print(driver_ids)

    for driver in driver_ids:
      rides = list(self.get_rides_2(driver, 3)) ## rides[0] = gps of 842 row data, rides[1] = gps of 958 row data, ...
      print(driver, len(rides))
      # print(len(rides[0]))

      test_x = [rides[i] for i in range(5)] ## len(test_x) = 20
      test_y = [driver for i in range(5)] ## len(test_y) = 20
      print("driver_id: {}\ntest_x: {}\n test_y: {}\n".format(driver, len(test_x), test_y))
      X.extend(test_x)
      Y.extend(test_y)

    return X, Y

  def get_random_rides(self, size, driver_id, seed=None, segments=False, version=1):
    if not seed:
      seed = random.Random(x=driver_id)
    drivers = self.get_random_drivers(size, seed, driver_id)
    for driver_id in drivers:
      ride_id = seed.randint(1, 200)
      if not segments:
        yield self.get_ride(driver_id, ride_id)
      else:
        yield self.get_ride_segments(driver_id, ride_id, version=version)