from PIL import Image

# Abra a imagem
imagem = Image.open('image/py.jpg')

# Obtém os dados dos pixels da imagem
dados_pixels = list(imagem.getdata())
print(dados_pixels[0])
# Feche a imagem
imagem.close()


def mod_cores_rgb(dados, r, g, b):
    dados_list = []
    for item in range(len(dados)):
        dados_list.append(list(dados[item]))
    for item in range(len(dados_list)):
        if dados_list[item][0] + r > 255:
            dados_list[item][0] = 255
        elif dados_list[item][0] + r < 0:
            dados_list[item][0] = 0
        else:
            dados_list[item][0] = dados_list[item][0] + r

        if dados_list[item][1] + g > 255:
            dados_list[item][1] = 255
        elif dados_list[item][1] + g < 0:
            dados_list[item][1] = 0
        else:
            dados_list[item][1] = dados_list[item][1] + g

        if dados_list[item][2] + b > 255:
            dados_list[item][2] = 255
        elif dados_list[item][2] + b < 0:
            dados_list[item][2] = 0
        else:
            dados_list[item][2] = dados_list[item][2] + b

    for item in range(len(dados_list)):
        dados_list[item] = tuple(dados_list[item])
        # print(item, dados_list[item])
    return dados_list


img = mod_cores_rgb(dados_pixels, 100, 100, 0)
print(type(dados_pixels))
print(type(img))

nova_imagem = Image.new(imagem.mode, imagem.size)
# nova_imagem.putdata(dados_pixels)
nova_imagem.putdata(img)

# Exiba a nova imagem
nova_imagem.save('./nova_imagem.png')
nova_imagem.show()


def qtd_cores(data):
    lista = set()
    for i in data:
        lista.add(i)

    print(len(lista))
    print(lista)


qtd_cores(img)
