import numpy as np
import scipy
import random
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.sparse import vstack
from sklearn.externals import joblib

from data_access import DataAccess
from model_def import Model_LR, Model_RFC, Model_SVC
import settings
import util_2

def get_data_movements_accel_2(model_id, driver_id, repeat, test=False, step=3, tf=False, extra=((1,15),2), version=1):
  seed = random.Random(x=sum(driver_id)+model_id)
  da = DataAccess()
  ngram_range, min_df = extra

  train_x, train_y = da.get_rides_train(driver_id, settings.BIG_CHUNK, segments=False) ## train set
  test_x, test_y = da.get_rides_test(driver_id, settings.SMALL_CHUNK, segments=False) ## test set

  set1 = train_x
  set2 = test_x

  set1 = [util_2.build_features4(r, i, step=step, version=version) for i, r in enumerate(set1)]
  set2 = [util_2.build_features4(r, i, step=step, version=version) for i, r in enumerate(set2)]

  if tf:
    vectorizer = TfidfVectorizer(min_df=min_df, ngram_range=ngram_range)
  else:
    vectorizer = CountVectorizer(min_df=min_df, ngram_range=ngram_range)

  set1 = vectorizer.fit_transform(set1)
  set2 = vectorizer.transform(set2)

  return set1, set2, train_y, test_y

def run_model_2(arr):
  model_id, driver_id, Model, get_data, repeat, multiplier = arr[0], arr[1], arr[2], arr[3], arr[4], 1

  ## check the parameters
  print("model_id: {}, driver_id: {}, Model: {}, get_data: {}, repeat: {}".format(model_id, driver_id, Model, get_data, repeat))

  trainX, testX, trainY, testY = get_data(model_id, driver_id, repeat)

  if type(trainX) in [scipy.sparse.csr.csr_matrix, scipy.sparse.coo.coo_matrix]:
    trainX = scipy.sparse.vstack(
        [trainX[:settings.BIG_CHUNK * multiplier]] * repeat +
        [trainX[settings.BIG_CHUNK * multiplier:]]
    )
  else:
    trainX = np.vstack((
        np.tile(np.array(trainX[:settings.BIG_CHUNK * multiplier]).T, repeat).T,
        trainX[settings.BIG_CHUNK * multiplier:]
    ))

  assert(trainX.shape[0] == len(trainY))
  assert(testX.shape[0] == len(testY))

  ## load existed model
  # model = joblib.load("myGpsClassificationModel.pkl")

  ## training model
  model = Model(trainX, trainY, driver_id)

  ## prediction
  predictions = model.predict(testX)

  return predictions, testY
