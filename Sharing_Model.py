from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np
from MainFuncs import get_sharing_dicts as dicts
from MainFuncs import prepare_train_input_for_C_Models as prepare

key_words = dicts()
c = 1
while c != len(key_words) + 1:
    name_of_model = 'Model_S' + str(c)
    current_dict = key_words[c - 1]
    input_data = np.array(prepare(current_dict) + [[0] * len(current_dict) * 2] + [[0] * len(current_dict) * 2])
    number_of_half_prob = len(current_dict) * 2
    number_of_true_prob = len(prepare(current_dict)) - len(current_dict) * 2
    output_data = np.array([[0.5]] * number_of_half_prob + [[1]] * number_of_true_prob + [[0]] + [[0]])
    model = Sequential()
    model.add(Dense(50, input_dim=len(current_dict) * 2))
    model.add(Activation('tanh'))
    model.add(Dense(1))
    model.add(Activation('tanh'))
    sgd = SGD(lr=0.1)
    model.compile(loss='mean_squared_error', optimizer=sgd)
    model.fit(input_data, output_data, batch_size=1, nb_epoch=10)
    model.save(name_of_model)
    c += 1
