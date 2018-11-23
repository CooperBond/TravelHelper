from MainFuncs import get_C_models
from MainFuncs import make_bigram
from MainFuncs import get_input
from MainFuncs import make_train_data
from MainFuncs import get_list_of_dictionaries as dicts
import numpy as np

models = get_C_models()
print('C - Models loaded')


def combine_text_to_network_vector(text):
    bigrams = make_bigram(text)
    p = 1
    result = []
    while p < len(dicts())+1:
        e = []
        e.append(p)
        e.append(0)
        result.append(e)
        p += 1
    result = dict(result)
    a = []
    for i in range(0, len(bigrams)):
        for j in range(0, len(models)):
            text = bigrams[i][0] + ' ' + bigrams[i][1]
            x = models[j].predict_proba(np.array(get_input(make_train_data(dicts()[j], text), dicts()[j])))
            a.append(x[0][0])

        for r in range(0, len(a)):
            if result[r + 1] == 0 or result[r + 1] < a[r]:
                result[r + 1] = a[r]

        a = []
    resulted = []
    for value in range(1, len(result) + 1):
        resulted.append(result[value])
    test_res = []
    for i in resulted:
        if i > 0.51:
            test_res.append(1)
        else:
            test_res.append(0)
    return test_res
