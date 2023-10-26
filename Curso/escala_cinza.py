import random
from pprint import pprint

from PIL import Image

# Abra a imagem RGB
imagem_rgb = Image.open('input/baloes.png')
# Converta a imagem para escala de cinza
imagem_cinza = imagem_rgb.convert('L')

# Salve a imagem em escala de cinza se desejar
imagem_cinza.save('imagem_cinza.png')
dados_pixels = list(imagem_cinza.getdata())
dados_pixels_set = set()
for i in dados_pixels:
    dados_pixels_set.add(dados_pixels[i])

print(dados_pixels_set)
# print(dados_pixels)
# Exiba a imagem em escala de cinza
imagem_cinza.show()

img = Image.open('imagem_cinza.png')


def modificar_imagem(imagem, mode, size):
    nova_imagem = Image.new(mode, size)
    dados = list(imagem.getdata())

    for i in range(len(dados)):
        if dados[i] <= 128:
            dados[i] = 0
        else:
            dados[i] = 255

    nova_imagem.putdata(dados)
    nova_imagem.save('imagem_modificada.png')
    nova_imagem.show()


modificar_imagem(img, img.mode, img.size)


def poluir_imagem(imagem, mode, size):
    nova_imagem = Image.new(mode, size)
    dados = list(imagem.getdata())
    percent = 0.01 * len(dados)
    print(int(percent))
    for i in range(int(percent)):
        dados[random.randint(0, len(dados))] = 255

    nova_imagem.putdata(dados)
    nova_imagem.save('imagem_poluida.png')
    nova_imagem.show()

    return nova_imagem


nova_imagem = poluir_imagem(img, img.mode, img.size)
# nova_imagem.show()