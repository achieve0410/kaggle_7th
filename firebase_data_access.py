import pyrebase
import numpy as np

config = {
  "apiKey": "#",
  "authDomain": "vlogger-driving-data.firebaseapp.com",
  "databaseURL": "https://vlogger-driving-data-160bb.firebaseio.com",
  "storageBucket": "vlogger-driving-data.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password('#', '#')

# Get a reference to the database service
db = firebase.database()

driver_path = 'test/trips'
driver_ids = db.child(driver_path).get().val().keys()
driver_ids = list(driver_ids)
# print(driver_ids)

for driver_idx, driver in enumerate(driver_ids):
  print(driver)
  date_path = driver_path + '/' + str(driver)
  dates = db.child(date_path).get().val().keys()
  dates = list(dates)
  # print(dates)

  for date in dates:
    # print(date)
    trip_path = date_path + '/' + str(date)
    trips = db.child(trip_path).get().val().keys()
    trips = list(trips)
    # print(trips)

    for trip_idx, trip in enumerate(trips):
      print(trip)
      point_path = trip_path + '/' + str(trip)

      ## no data trip exception
      if(db.child(point_path).get().val()==0):
        continue
      points = db.child(point_path).get().val().keys()
      points = list(points)
      # print(points)

      trip_data = []

      for point in points:
        print(point)
        data_path = point_path + '/' + str(point)
        data = db.child(data_path).get().val().keys()
        data = list(data)
        # print(data)

        latitude_path = data_path + '/latitude'
        latitude = db.child(latitude_path).get().val()
        longitude_path = data_path + '/longitude'
        longitude = db.child(longitude_path).get().val()

        # print("latitude, longitude: {}, {}".format(latitude, longitude))

        if(latitude!=None and longitude!=None):
          if([latitude, longitude] not in trip_data):
            print("latitude, longitude: {}, {}".format(latitude, longitude))
            trip_data.append([latitude, longitude])
      
      if(trip_data!=[]):
        np.savetxt(str(driver_idx) + '_' + str(trip_idx) + '.csv', trip_data, delimiter=',', fmt='%1.8f')
      print("\n\n trip data: {}\n\n".format(trip_data))
  
##############################################################################################################################
# test_path = 'test/trips/2n7HORuZsUdRmaMddyQttOJ2PqH3/201903/1552005998/1552006063'
# test = db.child(test_path).get().val().keys()

# latitude_path = test_path + '/latitude'
# latitude = db.child(latitude_path).get().val()
# longitude_path = test_path + '/longitude'
# longitude = db.child(longitude_path).get().val()

# print("latitude, longitude: {}, {}".format(latitude, longitude))
# if(latitude==None or longitude==None):
#   print("yes")
# else:
#   print("no")
##############################################################################################################################
