# DRIVER_IDS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# RIDE_IDS = [18, 11, 19, 77, 351, 35, 58, 8, 36, 4, 1, 12, 1, 9, 5, 19, 16, 2, 3, 31]

# DRIVER_IDS = [0, 1, 2, 3, 4, 5, 6, 8, 11, 15, 16, 19]
DRIVER_IDS = ['CL', 'R']
RIDE_IDS = [18, 11, 19, 77, 351, 35, 58, 8, 36, 4, 1, 12, 1, 9, 5, 19, 16, 2, 3, 31]

DATA_FOLDER = 'turn'
SEGMENTS_FOLDER = {
    1: 'segments', # used in final submission
    2: 'segments_v2', # not used
}

ENABLE_CACHE = True

CACHE = {
  1: 'cache_201fix_v2',
  2: 'cache_turbo2',
  4: 'cache_turbo',
  10: 'cache_turbo10',
  100: 'cache_turbo100',
}

BIG_CHUNK = 180
SMALL_CHUNK = 200 - BIG_CHUNK

FOLDS = 20
BIG_CHUNK_TEST = 200 * (FOLDS - 1) / FOLDS
SMALL_CHUNK_TEST = 200 - BIG_CHUNK_TEST
