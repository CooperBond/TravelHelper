from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np
from MainFuncs import get_train_input_u as input
from MainFuncs import get_train_output_u as output

X = np.array([[0] * 16] + input('U_Model_Data'))
Y = np.array([[0]] + output())

model = Sequential()
model.add(Dense(100, input_dim=16))
model.add(Activation('tanh'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

sgd = SGD(lr=0.1)
model.compile(loss='mean_squared_error', optimizer=sgd)

model.fit(X, Y, batch_size=1, nb_epoch=10)
model.save('U_Model')
