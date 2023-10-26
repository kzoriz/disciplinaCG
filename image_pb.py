from PIL import Image

imagem = Image.open('image/Facebook.png')
dados_pixels = list(imagem.getdata())
print(dados_pixels[0])


def mod_cores_rgb(dados, min, med, max):
    dados_list = []
    for item in range(len(dados)):
        dados_list.append(list(dados[item]))
    # binarizar imagem
    for item in range(len(dados_list)):
        if dados_list[item][2] < med:
            dados_list[item][2] = min
        elif dados_list[item][2] >= med:
            dados_list[item][2] = max
        if dados_list[item][3] < med:
            dados_list[item][3] = min
        elif dados_list[item][3] >= med:
            dados_list[item][3] = max

    # modificar
    for item in range(len(dados_list)):
        if dados_list[item][0] < med:
            dados_list[item][0] = min
        elif dados_list[item][0] >= med:
            dados_list[item][0] = max
        if dados_list[item][1] < med:
            dados_list[item][1] = min
        elif dados_list[item][1] >= med:
            dados_list[item][1] = max

    for item in range(len(dados_list)):
        dados_list[item] = tuple(dados_list[item])
        print(item, dados_list[item])
    return dados_list


img = mod_cores_rgb(dados_pixels, 0, 130, 255)
print(type(dados_pixels))
print(type(img))

nova_imagem = Image.new(imagem.mode, imagem.size)
# nova_imagem.putdata(dados_pixels)
imagem.close()
nova_imagem.putdata(img)

# Exiba a nova imagem
nova_imagem.save('./nova_imagem.png')
nova_imagem.show()


def qtd_cores(img):
    lista = set()
    for i in img:
        lista.add(i)

    print(len(lista))
    print(lista)


qtd_cores(img)
