import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten, Dropout
from keras.layers import LSTM
from keras import layers
import csv
import random
from keras import metrics
from numpy import asarray, newaxis
from keras.models import load_model


# Preload our model
model = load_model('./model/model.h5', compile=False)

def evaluate(gender, age, preexisting, symp1, persistent1, symp2, persistent2, symp3, persistent3, symp4, persistent4, symp5, persistent5, symp6, persistent6):
	# Preprocess data
	
	# Load model
	
	return


def predict(inputArray):

    prediction = model.predict(inputArray)

    return prediction
