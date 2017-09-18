#from __future__ import print_funtion
import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb
import csv
import random
from keras import metrics

max_features = 20000
#maxlen = 80 # cut text after this number of words
batch_size = 50

print('loading data...')

# Get the data
with open('inputs.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	trainingSet = list(reader)
random.shuffle(trainingSet)
train_data = trainingSet[:250]
test_data = trainingSet[250:]


training_feats = [featSet[:len(featSet)-1] for featSet in train_data]
# Extract training labels
training_labels = [labelSet[len(labelSet)-1] for labelSet in train_data]
# Convert labels to int for classification
training_ints = [int(float(i) * 100) for i in training_labels]
# Preprocess categical labels
training_labels = keras.utils.to_categorical(training_ints, num_classes=None)	

testing_feats = [featSet[:len(featSet)-1] for featSet in test_data]
# Extract testing labels
testing_labels = [labelSet[len(labelSet)-1] for labelSet in test_data]
# Convert labels (ICD9 codes) to int for clasification
testing_ints = [int(float(i) * 100) for i in testing_labels]
testing_labels = keras.utils.to_categorical(testing_ints, num_classes=None)

print('labels')


# Train dataset

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print('Train...')
model.fit(training_feats, training_labels, batch_size=batch_size, epochs=10, validation_data=(testing_feats, testing_labels))
score, acc = model.evaluate(testing_feats,testing_labels, batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
