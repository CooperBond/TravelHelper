from keras.models import load_model
from CombinationModule import combine_text_to_network_vector as comb
import numpy as np

global seas
global request

model = load_model('Initial_Response_Model_Traveling')
print('Traveling model is ready')
print('------------------------------------')

seasons = ['winter', 'spring', 'summer', 'autumn']
countries = []
accomodation = ['hotel', 'hostel', 'luxury hotel', 'apartment', 'economy_hotel', 'camping']
transport = ['car', 'motorcycle', 'bus', 'train', 'public_transport', 'bicycle', 'hitch_hiking']


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


def make_a(arrat):
    res = [0] * len(arrat)
    for i in range(0, len(arrat)):
        res[i] = arrat[i]
    return res


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


def vectorise_season(word):
    result = [0, 0, 0, 0]
    for i in range(0, len(seasons)):
        if word == seasons[i]:
            result[i] = 1
    return result


def get_season(text):
    global request
    request = text
    return 'Enter season'


def compile_resp(s):
    global seas
    seas = s
    print('Loading ...')
    h = model.predict_proba(np.array([comb(request) + vectorise_season(seas)]))
    array = h[0]
    cntrs = array[:len(countries)]
    hotels = array[len(countries):len(accomodation) + len(countries)]
    transp = array[len(accomodation) + len(countries):]
    response = ''
    response += 'Good variant will be ' + countries[find_max(cntrs)[1]] \
                + ', suggest you living in a ' + accomodation[find_max(hotels)[1]] \
                + ' , and your transport is ' + transport[find_max(transp)[1]] + '.'
    return response


prepare_countries()
