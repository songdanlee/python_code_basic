# -*- coding=utf-8 -*-
# 运行方式  ./ascii_dora.png -o '1.txt' --width 100  --height 50
from PIL import Image
# 命令行参数库
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

# file 必选位置参数
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #添加参数 -表示可选参数,用于一个字符，表示缩写，--也是可选参数，用于两个或以上的字符 输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):

    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    # 创建图片对象
    im = Image.open(IMG)
    # 重新调整图片指定大小，Image.NEAREST图像画质
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # The GetPixel function retrieves the red, green, blue (RGB) color value of the pixel at the specified coordinates.
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)