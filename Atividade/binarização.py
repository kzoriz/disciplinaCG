from PIL import Image


def convert_list_tuple(dados):
    for i in range(len(dados)):
        dados[i] = tuple(dados[i])

    return dados


# Abra a imagem
# img = Image.open('../Curso/imagem_cinza.png')
img = Image.open('../girasol.jpg')


def binarizacao(imagem, mode, size):
    nova_imagem = Image.new(mode, size)
    dados = list(imagem.getdata())

    for i in range(len(dados)):
        if dados[i] <= 128:
            dados[i] = 0
        else:
            dados[i] = 255

    nova_imagem.putdata(dados)
    nova_imagem.save('imagem_binarizada.png')
    # nova_imagem.show()

    return nova_imagem


imagem_binarizada = binarizacao(img, img.mode, img.size)
imagem_binarizada.show()
