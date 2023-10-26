from PIL import Image


image = Image.open('input/baloes.jpg')
print('JPG ', image.getpixel((100, 100)), image.size)

image2 = Image.open('input/py.jpg')
print('PNG ', image2.getpixel((100, 100)), image2.size)

image3 = Image.open('input/py.png')
print('PNG ', image3.getpixel((400, 130)), image3.size)

image4 = Image.open('input/py_balao.png')
print('PNG ', image4.getpixel((400, 130)), image4.size)

image.show()
image2.show()
image3.show()
image4.show()