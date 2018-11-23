from Sharing_CombineModule import make_sharing_model_check as mk
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np
from MainFuncs import get_sharing_dicts as dicts


def builder(text):
    element = ''
    for letter in text:
        if letter != '$':
            element += letter
        else:
            break
    return element


def prepare_input():
    text = open('DecisionModelData').read()
    element = ''
    x = ''
    for letter in text:
        if letter != '\n':
            element += letter
        else:
            x += element + ' ,'
            element = ''
    a = x.split(' ,')
    del a[len(a) - 1]
    inp = []
    out = []
    for i in range(0, len(a)):
        inp.append(a[i][:5])
        out.append(a[i][5:])
    resinp = []
    resout = []
    for element in inp:
        resinp.append(element.split(' '))
    for element in out:
        v = element.split(' ')
        del v[0]
        resout.append(v)
    final_inp = []
    final_out = []
    for j in range(0, len(resinp)):
        y = []
        for k in range(0, len(resinp[j])):
            y.append(int(resinp[j][k]))
        final_inp.append(y)
    for j in range(0, len(resout)):
        y = []
        for k in range(0, len(resout[j])):
            y.append(int(resout[j][k]))
        final_out.append(y)
    data = [final_inp, final_out]
    return data


s_dicts = dicts()
input_data = np.array(prepare_input()[0])
output_data = np.array(prepare_input()[1])
model = Sequential()
model.add(Dense(30, input_dim=len(s_dicts)))
model.add(Activation('tanh'))
model.add(Dense(3))
model.add(Activation('tanh'))
sgd = SGD(lr=0.1)
model.compile(loss='mean_squared_error', optimizer=sgd)
model.fit(input_data, output_data, batch_size=1, nb_epoch=17)
model.save('Initial_Decision_Model')
