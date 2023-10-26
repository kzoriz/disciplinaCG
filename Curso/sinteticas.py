from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"


def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)


def palestina(size1, size2):
    WHITE = (255, 255, 255)
    image = Image.new("RGB", (size1, size2), WHITE)
    for x in range(size1):
        for y in range(size2):
            if y < size2 / 3:
                image.putpixel((x, y), (7, 13, 13))
            if x < y:
                image.putpixel((x, y), (210, 35, 42))
            if y > -x + size2 and y > size1 / 3:
                image.putpixel((x, y), (255, 255, 255))
            if y > size2 * (2 / 3) and y > -x + size2 and y > size1 / 3:
                image.putpixel((x, y), (10, 124, 62))

    return image


palestina(800, 600).save('palestina.jpg')
palestina(900, 700).show()
