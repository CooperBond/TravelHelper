from MainFuncs import load_checking_model as chmo
from Sharing_CombineModule import make_sharing_model_check as mk
import numpy as np

model = chmo()


def make_dec(text):
    x = mk(text)
    h = model.predict_proba(np.array([x]))
    array = []
    for value in h[0]:
        if value > 0.4:
            array.append(1)
        else:
            array.append(0)
    return array
