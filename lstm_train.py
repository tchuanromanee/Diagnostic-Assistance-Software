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
	
print(training_feats)
print('labels')
print(training_labels)
#labels = trainingSet.ix[:,0].values.astype('int32')

#(x_train, y_train), (x_test, y_test) = load_data(num_words=max_features)
#print(len(x_train), 'train sequences')
#print(len(x_test), 'test sequences')

#print('Pad sequences (xamples x time)')
#x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
#x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
#print('x_train shape:', x_train.shape)
#print('x_test shape:', x_test.shape)

# Train dataset


print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train, batch_size=batch_size, epochs=15, validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
