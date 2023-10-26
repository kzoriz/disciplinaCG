from PIL import Image
import random

# Abra a imagem RGB

# img = Image.open('Curso/imagem_cinza.png')
img = Image.open('Atividade/imagem_monocromatica.png')


def poluir_imagem(imagem, mode, size):
    WHITE = 255
    #Cria nova imagem
    nova_imagem = Image.new(mode, size)
    #Pega os dados da imagem, converte em lista
    dados = list(imagem.getdata())
    #Converte as tuplas da lista em lista
    for i in range(len(dados)):
        dados[i] = list(dados[i])
    #percentual de poluição
    percent = 0.01 * len(dados)
    #se pixel for L
    if mode == 'L':
        for i in range(int(percent)):
            dados[random.randint(0, len(dados))] = WHITE
    #Se pixel for RGBA
    elif mode == 'RGBA':
        for i in range(int(percent)):
            pos = random.randint(0, len(dados))
            dados[pos][0] = WHITE
            dados[pos][1] = WHITE
            dados[pos][2] = WHITE
    else:
        print("formato ainda não permitido")
    #converte as listas da lista em tuplas
    for i in range(len(dados)):
        dados[i] = tuple(dados[i])
    #poe os dados na nova imagem
    nova_imagem.putdata(dados)
    #salva a nova imagem
    nova_imagem.save('imagem_poluida.png')

    return nova_imagem


nova_imagem = poluir_imagem(img, img.mode, img.size)
nova_imagem.show()
