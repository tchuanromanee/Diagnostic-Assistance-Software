#from __future__ import print_funtion

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb
import csv
import random

max_features = 20000
maxlen = 80 # cut text after this number of words
batch_size = 32

print('loading data...')

# Get the data
with open('inputs.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	trainingSet = list(reader)
random.shuffle(trainingSet)
train_data = trainingSet[:250]
test_data = trainingSet[250:]


training_feats = [featSet[:len(featSet)-1] for featSet in train_data]
training_labels = [labelSet[len(labelSet)-1] for labelSet in train_data]
	

testing_feats = [featSet[:len(featSet)-1] for featSet in test_data]
testing_labels = [labelSet[len(labelSet)-1] for labelSet in test_data]
print('labels')

# Train dataset

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print('Train...')
model.fit(training_feats, training_labels, batch_size=batch_size, epochs=5, validation_data=(testing_feats, testing_labels))
score, acc = model.evaluate(testing_feats,testing_labels, batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
