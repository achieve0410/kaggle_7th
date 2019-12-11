import logging

import model_run_2
import model_def
import settings
import util_2

logging.root.setLevel(level=logging.INFO)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

if __name__ == '__main__':
  logging.info('starting main.py')

  results = model_run_2.run_model_2( [100, settings.DRIVER_IDS[:10], model_def.Model_LR2, model_run_2.get_data_movements_accel_2, 1] )
  print("prediction: {}\ntestY: {}".format(results[0], results[1]))
