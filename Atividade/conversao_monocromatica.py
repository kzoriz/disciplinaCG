from PIL import Image
import random

# L = R * 299/1000 + G * 587/1000 + B * 114/1000
# Abra a imagem RGB
# img = Image.open('../Curso/input/baloes.png')
img = Image.open('../girasol.jpg')
img.show()


def conversao_monocromatica(imagem, mode, size):
    # WHITE = 255
    # BLACK = 0
    nova_imagem = Image.new(mode, size)
    dados = list(imagem.getdata())
    print(dados[0])
    for i in range(len(dados)):
        dados[i] = list(dados[i])
    print(dados[0])
    for i in range(len(dados)):
        r = int(dados[i][0] * 299 / 1000)
        g = int(dados[i][1] * 587 / 1000)
        b = int(dados[i][2] * 114 / 1000)
        cor = int(r + g + b / 1000)
        dados[i][0] = cor
        dados[i][1] = cor
        dados[i][2] = cor
    for i in range(len(dados)):
        dados[i] = tuple(dados[i])
    nova_imagem.putdata(dados)
    nova_imagem.save('imagem_monocromatica.png')
    # nova_imagem.show()

    return nova_imagem


imagem_monocromatica = conversao_monocromatica(img, img.mode, img.size)
imagem_monocromatica.show()
