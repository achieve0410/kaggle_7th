import random
from datetime import datetime

import settings

class DataAccess:


  def get_ride(self, driver_id, ride_id):
    filename = '%s/%s/%s.csv' % (settings.DATA_FOLDER, driver_id, ride_id)
    data = open(filename, 'r').read()
    data = [[float(x) for x in row.split(',')] for row in data.split('\n')[1:-1]]

    return data

  def get_rides(self, driver_id):
    for ride_id in range(1, 201):
      yield self.get_ride(driver_id, ride_id)

  def get_rides_2(self, driver_id, size):
    for ride_id in range(1, size+1):
      yield self.get_ride(driver_id, ride_id)

  def get_rides_train(self, driver_ids, size_train, segments=False, version=1):
    seed = random.Random(x=datetime.now())
    X = []
    Y = []

    for driver in driver_ids:
      rides = list(self.get_rides(driver)) ## rides[0] = gps of 842 row data, rides[1] = gps of 958 row data, ...

      train_x = [rides[i] for i in range(200)] ## len(train_x) = 200
      train_y = [driver for i in range(200)] ## len(train_y) = 200

      X.extend(train_x)
      Y.extend(train_y)

    return X, Y

  def get_rides_test(self, driver_ids, size_test, segments=False, version=1):
    seed = random.Random(x=datetime.now())
    driver_id = set([driver_ids[i] for i in seed.sample(range(len(driver_ids)), 4)])
    X = []
    Y = []

    for driver in driver_id:
      rides = list(self.get_rides_2(driver, size_test)) ## rides[0] = gps of 842 row data, rides[1] = gps of 958 row data, ...

      test_x = [rides[i] for i in range(size_test)] ## len(test_x) = 20
      test_y = [driver for i in range(size_test)] ## len(test_y) = 20

      X.extend(test_x)
      Y.extend(test_y)

    return X, Y