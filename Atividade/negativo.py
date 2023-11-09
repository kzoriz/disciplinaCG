from PIL import Image
from utils import *


# Abra a imagem
# img = Image.open('../Curso/imagem_cinza.png')
img = Image.open('imagem_monocromatica.png')


def negativo(imagem, mode, size):
    nova_imagem = Image.new(mode, size)
    dados = list(imagem.getdata())
    data = convert_list_tuple(dados)

    for i in range(len(dados)):
        data[i][0] = 255 - data[i][0]
        data[i][1] = 255 - data[i][1]
        data[i][2] = 255 - data[i][2]
    data = convert_list_tuple(data)
    nova_imagem.putdata(data)
    nova_imagem.save('imagem_negativa.png')
    # nova_imagem.show()

    return nova_imagem


imagem_negativa = negativo(img, img.mode, img.size)
imagem_negativa.show()
