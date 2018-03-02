import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten, Dropout
from keras.layers import LSTM
from keras import layers
from keras.datasets import imdb
import csv
import random
from keras import metrics
from numpy import asarray, newaxis
from keras.models import load_model


# Preload our model
print("Loading model")
model = load_model('./model/model.h5', compile=False)


THRESHOLD = 0.5
@app.route('/predict', methods=['POST'])
def predict(inputArray):

    prediction = model.predict(inputArray)
    print('PREDICTION COUNT', (prediction[:, :, 1]>0.5).sum())

    return
