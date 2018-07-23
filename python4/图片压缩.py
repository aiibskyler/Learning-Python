from PIL import Image
import os

def getPicSize(srcImg):
    fileSize = os.path.getsize(srcImg)
    return  fileSize

def pic(srcImg):
    fileSize = getPicSize(srcImg)
    im = Image.open(srcImg)
    siz = im.size
    if fileSize>10240:
        width = round(siz[0] * 0.5)
        height = round(siz[1] * 0.5)
        im.thumbnail((width, height))
        im.save("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg", "JPEG")
    else:
        im.save("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg", "JPEG")

def main(srcImg):
    #srcImg = input("请输入地址")
    pic(srcImg)
    testSize = "C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg"
    im = Image.open(testSize)
    if getPicSize(testSize)>10240:
        main(testSize)
    else:
        im.save("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg", "JPEG")

srcImg = "C:\\Users\\linzh\\Desktop\\PPT背景图片\\03793_canyonlands_6400x4000.jpg"
main(srcImg)