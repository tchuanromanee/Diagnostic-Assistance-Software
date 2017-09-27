#from __future__ import print_funtion
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

max_features = 20000
#maxlen = 80 # cut text after this number of words
batch_size = 250

print('loading data...')

# Get the data
with open('inputs_catformat.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	trainingSet = list(reader)
random.shuffle(trainingSet)
train_data = trainingSet[:250]
test_data = trainingSet[250:]


training_feats = [featSet[:len(featSet)-1] for featSet in train_data]

# Extract training labels
training_labels = [labelSet[len(labelSet)-1] for labelSet in train_data]
# Convert labels to int for classification
#training_ints = [int(float(i) * 100) for i in training_labels]
# Preprocess categical labels
training_labels = keras.utils.to_categorical(training_labels, num_classes=None)	

testing_feats = [featSet[:len(featSet)-1] for featSet in test_data]
# Extract testing labels
testing_labels = [labelSet[len(labelSet)-1] for labelSet in test_data]
# Convert labels (ICD9 codes) to int for clasification
#testing_ints = [int(float(i) * 100) for i in testing_labels]
testing_labels = keras.utils.to_categorical(testing_labels, num_classes=None)

# Convert to numpy arrays
training_feats = asarray(training_feats)
#training_feats = training_feats.reshape(training_feats.shape[0],15)
#training_feats = training_feats[:,:,newaxis]i
#training_feats = training_feats[0]
training_labels = asarray(training_labels)
testing_feats = asarray(testing_feats)
testing_labels = asarray(testing_labels)


num_features = training_feats.shape[1]

# Train dataset

print('Build model...')
model = Sequential()
#model.add(Embedding(max_features, 128))
#model.add(LSTM(128,input_dim = num_features, dropout=0.2, recurrent_dropout=0.2))
#model.add(Dense(2, activation='sigmoid'))
#model.add(Dense(128, input_dim = num_features))

## Curent testing
#model.add(Embedding(128,15))
#
#model.add(Dense(100, batch_input_shape=(batch_size,15)))

model.add(Dense(50, batch_size=batch_size,activation='relu', input_dim=15))
model.add(Dense(19, activation='softmax'))

#model.add(LSTM(100, batch_input_shape=(batch_size,15,1), return_sequences=True))
#model.add(layers.Activation('softmax'))

#model.add(Dense(78840, input_shape=(15,)))
#model.add(Dropout(0.5))
#model.add(LSTM(50, return_sequences=True))
#model.add(Flatten())
#model.add(Dense(78840))

model.summary()

# try using different optimizers and different optimizer configs
model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

print('Train...')
model.fit(training_feats, training_labels, batch_size=batch_size, epochs=10, validation_data=(testing_feats, testing_labels))
score, acc = model.evaluate(testing_feats,testing_labels, batch_size=50)
print('Test score:', score)
print('Test accuracy:', acc)
