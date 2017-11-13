from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input file')
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('--width', type=int, help='width of image', default=50)
parser.add_argument('--height', type=int, help='height of image', default=50)

args = parser.parse_args()
input = args.input
output = args.output
width = args.width
height = args.height

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# chars = "jft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxr"
length = len(chars)


def image2char(_tuple):
    r = _tuple[0]
    g = _tuple[1]
    b = _tuple[2]
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return chars[int(gray / 256.0 * length)]


def main():
    image = Image.open(input)
    image = image.resize((width, height))

    txt = ""
    for i in range(height):
        for j in range(width):
            txt += image2char(image.getpixel((j, i)))
        txt += "\n"

    with open(output, 'a') as f:
        f.write(txt)


if __name__ == '__main__':
    main()
