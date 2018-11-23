from MainFuncs import prepare_train_input_for_C_Models as prep
from MainFuncs import get_list_of_dictionaries as dicts
from MainFuncs import make_vector_by_category as m
from CombinationModule import combine_text_to_network_vector as comb
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy as np

input_data = []
output_data = []
seasons = ['winter', 'spring', 'summer', 'autumn']

countries = []
accomodation = ['hotel', 'hostel', 'luxury hotel', 'apartment', 'economy_hotel', 'camping']
transport = ['car', 'motorcycle', 'bus', 'train', 'public_transport', 'bicycle', 'hitch_hiking']


def make_train_output(text):
    result1 = [0] * len(countries)
    result2 = [0] * len(accomodation)
    result3 = [0] * len(transport)

    a = text.split(' ')
    country = a[0]
    acc = a[1]
    transp = a[2]

    for i in range(0, len(countries)):
        if country == countries[i]:
            result1[i] = 1
            break
    for i in range(0, len(accomodation)):
        if acc == accomodation[i]:
            result2[i] = 1
            break
    for i in range(0, len(transport)):
        if transp == transport[i]:
            result3[i] = 1
            break
    result = result1 + result2 + result3
    print('Output: ', result)
    return result


def vectorise_season(word):
    result = [0, 0, 0, 0]
    for i in range(0, len(seasons)):
        if word == seasons[i]:
            result[i] = 1
    return result


def make_train_input(path):
    x = ''
    element = ''
    for word in open(path).read():
        if word != '\n':
            element += word
        else:
            x += element + ' ,'
            element = ''
    a = x.split(' ,')
    del a[len(a) - 1]
    for i in range(0, len(a)):
        request = ''
        season = ''
        ans = ''
        inp = a[i]
        index = 0
        for j in range(1, len(inp)):
            if inp[j] == ']':
                index = j
                break
            else:
                ans += inp[j]
        for j in range(index + 1, len(inp)):
            if inp[j] != '(':
                request += inp[j]
            else:
                season = inp[j + 1:len(inp) - 1]
                break
        input_data.append(comb(request) + vectorise_season(season))
        print(comb(request) + vectorise_season(season))
        output_data.append(make_train_output(ans))


def prepare_countries():
    c = open('countries').read()
    x = ''
    element = ''
    for word in c:
        if word != '\n':
            element += word
        else:
            x += element + ' ,'
            element = ''
    a = x.split(' ,')
    del a[len(a) - 1]
    for v in a:
        countries.append(v)


prepare_countries()
make_train_input('Initial_response_Data')

X1 = np.array(input_data)
Y1 = np.array(output_data)
model1 = Sequential()
model1.add(Dense(50, input_dim=len(dicts()) + 4))
model1.add(Activation('relu'))
model1.add(Dense(len(countries) + len(transport) + len(accomodation)))
model1.add(Activation('sigmoid'))
sgd = SGD(lr=0.1)
model1.compile(loss='mean_squared_error', optimizer=sgd)
model1.fit(X1, Y1, batch_size=1, nb_epoch=10)
model1.save('Initial_Response_Model_Traveling')


def find_max(array):
    index = 0
    a = make_a(array)
    max = a[index]
    response = []
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
            index = i
    response.append(max)
    response.append(index)
    return response


def make_a(arrat):
    res = [0] * len(arrat)
    for i in range(0, len(arrat)):
        res[i] = arrat[i]
    return res


def compile_response(array):
    cntrs = array[:len(countries)]
    hotels = array[len(countries):len(accomodation) + len(countries)]
    transp = array[len(accomodation) + len(countries):]
    response = ''
    response += 'Good variant will be ' + countries[find_max(cntrs)[1]] \
                + ', suggest you living in a ' + accomodation[find_max(hotels)[1]] \
                + ' , and your transport is ' + transport[find_max(transp)[1]] + '.'
    return response



