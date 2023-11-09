from PIL import Image
from utils import *

# Abra a imagem
# img = Image.open('../Curso/imagem_cinza.png')
img = Image.open('imagem_monocromatica.png')


def limiarizacao(imagem, mode, size):

    try:
        qtd = int(input("quantos limiares?"))

        valor = 255 // qtd
        print(valor)
        nova_imagem = Image.new(mode, size)
        dados = list(imagem.getdata())
        data = convert_list_tuple(dados)
        limiar = valor
        valor_ant = 0
        cont = 0
        while limiar <= 255:
            if limiar > 255:
                limiar = 255
            for j in range(len(data)):
                if valor_ant < data[j][0] < limiar:
                    # print(valor_ant, limiar)
                    data[j][0], data[j][1], data[j][2] = limiar - ((limiar - valor_ant) // 2), \
                        (limiar - (limiar - valor_ant) // 2), \
                        (limiar - (limiar - valor_ant) // 2)
                    print(f'se estiver entre {valor_ant} e {limiar}, recebe {limiar - ((limiar - valor_ant) // 2)}')
            valor_ant = limiar
            limiar += valor
            # if limiar > 255:
            #     limiar = 255
            cont += 1
            print(limiar)
            print(cont)
        data = convert_list_tuple(data)
        # print_img(data)
        nova_imagem.putdata(data)
        nova_imagem.save('imagem_limiarizada.png')
        # nova_imagem.show()

        return nova_imagem
    except:
        print("informe um numero")


imagem_limiar = limiarizacao(img, img.mode, img.size)
imagem_limiar.show()
