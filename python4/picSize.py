from PIL import Image
import os
srcImg="C:\\Users\\linzh\\Desktop\\PPT背景图片\\sadsa.jpg"
fileSize = os.path.getsize(srcImg)
im = Image.open(srcImg)
siz = im.size
print(siz)
if siz[0]>200 and siz[1]>200:
    width = round(siz[0]*0.1)
    height = round(siz[1]*0.1)
    im.thumbnail((width, height))
    im.save("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg", "JPEG")

else:
    width=siz[0]
    height=siz[1]
    print(width,height)
    im.thumbnail((width,height))
    im.save("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg","JPEG")


# img = Image.open("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC009.jpg")
# if im.size[0] > 1024 or im.size[1] > 1000:
#     width = 1024
#     height = float(1024) / im.size[0] * im.size[1]
# im.thumbnail((width,height),Image.ANTIALIAS)
# im.save("C:\\Users\\linzh\\Desktop\\PPT背景图片\\_DSC.jpg","JPEG")

