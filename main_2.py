import logging
import multiprocessing
import itertools

import numpy as np

from model_run_2 import run_model, test_model
import model_run_2
import model_def
import settings
import util_2

logging.root.setLevel(level=logging.INFO)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

if __name__ == '__main__':
  logging.info('starting main.py')

  #run_model((100, 203, model_def.Model_GBC, model_run.get_data_accel_v2_svd, 1)); raise Exception
  results = model_run_2.run_model_2( [100, settings.DRIVER_IDS[:10], model_def.Model_LR2, model_run_2.get_data_movements_accel_2, 1] )

  # pool = multiprocessing.Pool(processes=1)
  # results = pool.map(
      # run_model,
      # map(lambda x: [100, x, model_def.Model_LR2, model_run_2.get_data_movements_accel, 1], settings.DRIVER_IDS[:5])
      # model_run_2.run_model_2,
      # map(lambda x: [100, x, model_def.Model_LR2, model_run_2.get_data_movements_accel, 1], settings.DRIVER_IDS[:5])
  # )
  print("prediction: {}\ntestY: {}".format(results[0], results[1]))
  # predictions = np.array(list(itertools.chain(*[r[0] for r in results])))
  # testY = list(itertools.chain(*[r[-1] for r in results]))
  # print("results: {}\ntestY: {}\npredictions :{}".format(results, testY, predictions))
  print(results[0][0], results[0][1], results[1], results[2])
  # print(len(results), len(testY), len(predictions))
  # logging.info(util.compute_auc(testY, predictions))
