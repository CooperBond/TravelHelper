from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np
from MainFuncs import get_list_of_dictionaries as dicts
from MainFuncs import prepare_train_input_for_C_Models as prepare

count_of_models = len(dicts())
count = 0
while count != count_of_models:
    name_of_model = 'ModelC' + str(count + 1)
    print(name_of_model)
    key_words = dicts()[count]
    input_data = np.array(prepare(key_words) + [[0] * len(key_words) * 2] + [[0] * len(key_words) * 2])
    number_of_half_prob = len(key_words) * 2
    number_of_true_prob = len(prepare(key_words)) - len(key_words) * 2

    output_data = np.array(
        [[0.5]] * number_of_half_prob + [[1]] * number_of_true_prob + [[0]] + [[0]])

    model = Sequential()
    model.add(Dense(100, input_dim=len(key_words) * 2))
    model.add(Activation('tanh'))
    model.add(Dense(1))
    model.add(Activation('tanh'))

    sgd = SGD(lr=0.1)
    model.compile(loss='mean_squared_error', optimizer=sgd)

    model.fit(input_data, output_data, batch_size=1, nb_epoch=10)

    model.save(name_of_model)
    count += 1
