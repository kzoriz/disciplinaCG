from PIL import Image
from utils import *

# Abra a imagem
# img = Image.open('../Curso/imagem_cinza.png')
img = Image.open('imagem_monocromatica.png')


def binarizacao(imagem, mode, size):
    nova_imagem = Image.new(mode, size)
    dados = list(imagem.getdata())
    data = convert_list_tuple(dados)

    for i in range(len(data)):
        if data[i][0] <= 168:
            data[i][0], data[i][1], data[i][2] = 0, 0, 0

        else:
            data[i][0], data[i][1], data[i][2] = 255, 255, 255

    data = convert_list_tuple(dados)
    nova_imagem.putdata(data)
    nova_imagem.save('imagem_binarizada.png')
    # nova_imagem.show()

    return nova_imagem


imagem_binarizada = binarizacao(img, img.mode, img.size)
imagem_binarizada.show()
