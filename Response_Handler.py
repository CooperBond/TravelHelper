from MakeDecisionModule import make_dec as md
from Response_Travel import get_season as gets
from Response_Travel import vectorise_season as vs
from Response_Travel import compile_resp as comp
from Sharing_CombineModule import make_sharing_model_check as mk


def say_hello(param):
    return 'Hello!'


def flud_response(param):
    return 'Do not flood , I am a banana'


list_of_funcs = [say_hello, gets, flud_response]
seasons = ['winter', 'spring', 'summer', 'autumn']


def m_response(text):
    answer = ''
    for e in seasons:
        if text == e:
            return comp(text)
    array = mk(text)
    for i in range(0, len(array)):
        if array[i] == 1:
            answer += (list_of_funcs[i](text)) + '\n'
    return answer
