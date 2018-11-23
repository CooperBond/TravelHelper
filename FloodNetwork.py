from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np

dictioanary = []
input_data = np.array()
output_data = np.array()
model = Sequential()
model.add(Dense(30, input_dim=len(dictioanary)))
model.add(Activation('tanh'))
model.add(Dense(3))
model.add(Activation('tanh'))
sgd = SGD(lr=0.1)
model.compile(loss='mean_squared_error', optimizer=sgd)
model.fit(input_data, output_data, batch_size=1, nb_epoch=10)

# TODO
# This network should make few networks to realize content of flood
# It might be: question or sentence
# Then : Q:about program or just other flood

