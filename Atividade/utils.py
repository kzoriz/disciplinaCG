def convert_list_tuple(dados):
    if type(dados[0]) == list:
        print('list')
        for i in range(len(dados)):
            dados[i] = tuple(dados[i])
    elif type(dados[0]) == tuple:
        print('tuple')
        for i in range(len(dados)):
            dados[i] = list(dados[i])

    return dados


def print_img(img_data):
    for i in img_data:
        print(i)
