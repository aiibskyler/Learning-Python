from PIL import Image, ImageFilter

im = Image.open('../images/photo-brendan-lynch-n-210.jpg')
r,g,b=im.split()
om = Image.merge("RGB",(b,g,r))
om= om.filter(ImageFilter.BLUR)
om.save('../images/ChangeRGB - photo-brendan-lynch-n-210.jpg')