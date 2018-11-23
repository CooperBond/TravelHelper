from keras.models import load_model


def make_bigram(test):
    test_list = test.split(' ')
    a = []
    for word in test_list:
        if word == 'and' \
                or word == 'the' \
                or word == 'a' \
                or word == ',' \
                or word == '.' \
                or word == ';' \
                or word == ':' \
                or word == '!':
            del word
        else:
            a.append(word.lower())
    pairs = []
    temp = []
    count = 0
    i = 0
    while i != len(a):
        temp.append(a[i])
        count += 1
        i += 1
        if count == 2:
            pairs.append(temp)
            i = i - 1
            count = 0
            temp = []
    return pairs


def make_vector_by_category(list_data, dict_data):
    x_x = [[0] * len(dict_data), [0] * len(dict_data)]
    final_data = []
    for i_2 in range(0, len(list_data)):
        a_2 = list_data[i_2]
        for v in range(0, len(a_2)):
            for x in range(0, len(dict_data)):
                if a_2[v] == dict_data[x]:
                    x_x[v][x] = 1
        final_data.append(x_x)
        x_x = [[0] * len(dict_data), [0] * len(dict_data)]
    return final_data


def get_list_of_dictionaries():
    dict_list = []

    car = 'drive car vehicle rv jeep sport engine fuel gas truck wheel wheels bumper seats driving'
    bus = 'bus tourist exhibitions excursions popular guide people'
    bicycle = 'bicycle bicycles brakes caravan jump eco ecological'
    legs_public_transport = 'legs foot public trolley tram taxi'
    train = 'train intercity'
    airplane = 'plane airplane flight fly'
    hitch_hiking = 'hitch hiking'
    family = 'family kids husband wife girlfriend'
    friends = 'friend friends party parties fun alcohol trash extrovert'
    only_one = 'me introvert quiet only'
    colleagues = 'colleagues'
    high_budget = 'expensive luxury vip lot huge big high'
    middle_budget = 'middle usual average'
    low_budget = 'small low economy cheap cost free'
    hot_weather = 'hot beach sea water desert sunny light'
    cold_weather = 'cold ice snow snowy icy mount mounts'
    raining = 'rain rains spring autumn'
    cloudy = 'cloudy cloud clouds'
    windily = 'wind winds'
    sunny = 'sunny sun shining'
    changing_weather = 'different changing'
    rest = 'sanatorium rest cruise'
    entertainment = 'kayaks bar bars bowling cafe cafes club clubs'
    architecture = 'architecture architect building buildings house houses famous'
    nature = 'nature landscape sunrise sundown sky camps forest forests river rivers hiking camp camping'
    extreme = 'war pirates robbery rob weapon knife kill police gangsta'
    east = 'eastern east asian russian russia'
    west = 'west western'
    south = 'south southern african africa'
    north = 'north northern'
    business = 'business work job meeting conference team head department firm office'

    prelist = [car, bus, bicycle, family, friends, only_one, high_budget, middle_budget, low_budget,
               hot_weather, cold_weather, architecture, nature, extreme, business, rest, entertainment,
               raining, windily, cloudy, sunny, changing_weather, colleagues, hitch_hiking, train,
               airplane, legs_public_transport]
    for element in prelist:
        dict_list.append(element.split(' '))
    return dict_list


def make_train_data(key_words, text):
    list_t = text.split(' ')
    final_list = []
    result_input = []
    for word in list_t:
        if word == 'and' \
                or word == 'the' \
                or word == 'a' \
                or word == ',' \
                or word == '.' \
                or word == ';' \
                or word == ':' \
                or word == '!':
            del word
        else:
            final_list.append(word.lower())
    for i in range(0, len(final_list)):
        a = []
        for j in range(0, len(key_words)):
            if final_list[i] == key_words[j]:
                if i == 0:
                    a.append(final_list[i])
                    a.append(final_list[i + 1])
                    result_input.append(a)
                    a = []
                elif i == len(final_list) - 1:
                    a.append(final_list[i - 1])
                    a.append(final_list[i])
                    result_input.append(a)
                    a = []
                else:
                    a.append(final_list[i])
                    a.append(final_list[i - 1])
                    result_input.append(a)
                    a = []
                    a.append(final_list[i])
                    a.append(final_list[i + 1])
                    result_input.append(a)
                    a = []

    return result_input


def make_one_array(array):
    result = []
    for value in array[0]:
        result.append(value)
    for value2 in array[1]:
        result.append(value2)
    return result


def prepare_combinations(dict_data):
    import itertools
    anyword = 'anyword'
    result = []
    element = []
    for i in range(0, len(dict_data)):
        element.append(dict_data[i])
        element.append(anyword)
        result.append(element)
        element = []
    for i in range(0, len(dict_data)):
        element.append(anyword)
        element.append(dict_data[i])
        result.append(element)
        element = []
    combinations = list(itertools.product(dict_data, dict_data))
    a_combs = []
    for tup in combinations:
        e = tup[:]
        a_combs.append(e)
    for arr in a_combs:
        result.append(arr)
    print(result)
    return result


def prepare_train_input_for_C_Models(dict_data):
    result = prepare_combinations(dict_data)
    prepared_batch = []
    for i in range(0, len(result)):
        array_1 = [0] * len(dict_data)
        array_2 = [0] * len(dict_data)
        for j in range(0, len(result[i])):
            for k in range(0, len(dict_data)):
                if j != 1:
                    if result[i][j] == dict_data[k]:
                        array_1[k] = 1
                else:
                    if result[i][j] == dict_data[k]:
                        array_2[k] = 1
        a = [array_1, array_2]
        prepared_batch.append(make_one_array(a))

    return prepared_batch


def get_input(text_data, m_dict):
    result = []
    pre_result = make_vector_by_category(text_data, m_dict)
    if len(text_data) == 0:
        return [[0] * len(m_dict) * 2]
    for element in pre_result:
        result.append(make_one_array(element))
    return result


def get_test_input(text, m_dict):
    a = make_vector_by_category(make_train_data(m_dict, text), m_dict)
    if len(a) == 0:
        return [[0] * len(m_dict) * 2]
    return make_one_array(a[0])


def get_C_models():
    count = len(get_list_of_dictionaries())
    c = 0
    model_name = 'ModelC'
    models = []
    while c != count:
        x = c + 1
        model_name += str(x)
        model = load_model(model_name)
        print('Model ', x, ' loaded')
        models.append(model)
        model_name = 'ModelC'
        c += 1
    return models


def get_train_input_u(path):
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
    vector = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
    b = []
    for string in a:
        int_array = []
        e = string.split(' ')
        for symb in e:
            int_array.append(int(symb))
        b.append(int_array)
    result = []
    for v in b:
        pre = [0] * 16
        for i in v:
            if i != 0:
                vector[i] = 1
        for key, value in vector.items():
            if value != 0:
                pre[key - 1] = 1
        result.append(pre)
        vector = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
    return result


def get_train_output_u():
    all_data = get_train_input_u('U_Model_Data')
    true_data = get_train_input_u('true_input_data')
    pre_result = [[0]] * len(all_data)
    for i in range(0, len(all_data)):
        element = []
        for j in range(0, len(true_data)):
            if all_data[i] == true_data[j]:
                element.append(1)
                pre_result[i] = element
                break
    result = []
    for k in range(0, len(pre_result)):
        if pre_result[k][0] == 0:
            result.append([0.5])
        else:
            result.append([1])
    result[0][0] = 0
    return result


def get_sharing_dicts():
    greetings = 'hello hi evening morning day'
    main = 'travel trip want country journey'
    flud = 'can possible master how'
    dicts = [greetings, main, flud]
    dict_list = []
    for element in dicts:
        dict_list.append(element.split(' '))
    return dict_list


def get_S_models():
    count = len(get_sharing_dicts())
    c = 0
    model_name = 'Model_S'
    models = []
    while c != count:
        x = c + 1
        model_name += str(x)
        model = load_model(model_name)
        print('Model ', x, ' loaded')
        models.append(model)
        model_name = 'Model_S'
        c += 1
    return models


def load_checking_model():
    model = load_model('Initial_Decision_Model')
    return model
