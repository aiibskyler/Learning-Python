#做自己的词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
from PIL import Image

import jieba
words=''
with open('C:\\Users\\lenovo\\Downloads\\红楼梦.txt', "r",encoding=" utf-8" ) as hlm:
     for line in hlm. readlines():
        line=line.strip('\n' )
        words+=''.join(jieba.cut(line))
        words=words.replace('道','')
        words=words.replace('笑','')
        words+=''
#处理自己的数据
# filename="arthas.txt"
# with open(filename."r")as f:
#     arthastxt=f.read()
bimg=plt.imread("C:\\Users\\lenovo\\Desktop\\555.jpg")  #读图片

wordcloud=WordCloud(relative_scaling=0.8,background_color=None,mode="RGBA",
                    mask=bimg, font_path='C:/Windows/Fonts/msyh.ttc', stopwords=STOPWORDS.add('说着')).generate(words)

image_colors = ImageColorGenerator(bimg)
wordcloud.recolor(color_func=image_colors)
plt.imshow(wordcloud,interpolation='nearest')
plt.axis("off")
plt.savefig('C:\\Users\\lenovo\\Desktop\\521.jpg')
#wordcloud.to_file('C:\\Users\\lenovo\\Desktop\\523.jpg')
