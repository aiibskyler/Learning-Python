from PIL import Image
ascii_char = list('$@B%8&WM#*oahkbdpqwmzo0QLCJUYXzxcvnxrjf\
                  1234567895t/\|1{}[]?-_+`<>i!;:,\",')
def get_char(r,g,b,alpha=256):
    if alpha == 0:
        return ''
    gray = int(0.2126 * r +0.7152 * g + 0.0722*b)
    unit = 256/len(ascii_char)
    return ascii_char[int(gray//unit)]

def main():
    im = Image.open('C:\\Users\\linzh\\Desktop\\PPT背景图片\\MC.jpg')
    WIDTH,HEIGHT=130,60
    im= im.resize((WIDTH,HEIGHT))
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt +='\n'
    fo = open("C:\\Users\\linzh\\Desktop\\PPT背景图片\\pic_char.txt","w")
    fo.write(txt)
    fo.close()

main()