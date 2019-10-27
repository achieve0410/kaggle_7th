import json
import numpy as np

with open('vlogger_data.json', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

    driver_path = json_data['test']['trips']
    drivers = list(driver_path.keys())
    # print(drivers)

    for driver_idx, driver in enumerate(drivers):
        date_path = driver_path[driver]
        dates = list(date_path.keys())
        # print(driver, dates)

        trip_count = 0
        for date in dates:
            trip_path = date_path[date]
            
            ## error handling
            if(date=='null'):
                print('\n\n in driver: {}, date: {}'.format(driver, date))
                print("\n\ndate is null\n\n")
                continue
            else:
                trips = list(trip_path.keys())
                # print(trips)

            for trip in trips:
                # print(trip)
                point_path = trip_path[trip]
                # print(type(point_path))

                ## error handling
                if(type(point_path)==int):
                    continue
                else:
                    # print(point_path)
                    points = list(point_path.keys())
                    # print(points)

                    trip_data = []                
                    for point in points:
                        data_path = point_path[point]
                        if('latitude' in data_path.keys() and 'longitude' in data_path.keys()):
                            latitude = data_path['latitude']
                            longitude = data_path['longitude']
                            # print(latitude, longitude)
                    
                            if(latitude!=None and longitude!=None):
                                if([latitude, longitude] not in trip_data):
                                    trip_data.append([latitude, longitude])
                        else:
                            print("\nla and long not exist\n")

                    if(trip_data!=[]):
                        np.savetxt(str(driver_idx) + '_' + str(trip_count) + '.csv', trip_data, delimiter=',', fmt='%1.8f')            
                        print(trip_data, len(trip_data))
                        trip_count += 1




    
    # test = dict(driver_path['LffKUSOr9CQqmOrqVOGjqTEChIv1']['null']).keys()
    # test = dict(driver_path['MOkhJKsy4GNZkDmhSR0eOFfneZj2']['201906']).keys()
    # test = driver_path['87Ud4UycQZSsWqKd3Tt05c5FdIA2']['null'].keys()
    print(test)
