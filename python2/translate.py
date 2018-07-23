import requests
import sys

# 如果没有从命令行传入待查单词，就从键盘输入
if len(sys.argv) < 2:
    word = input("What word do you want to translate? ")
    sys.argv.append(word)

# 获取单词
word = sys.argv[1]
url = 'http://fanyi.baidu.com/sug'
# 构建post数据
data = {'kw': word}
res = requests.post(url, data=data)
# 获取结果，用json解析
res_json = res.json()
# 如果errno的值大于0说明查询的单词无效
if res_json['errno'] > 0:
    print("Check spelling!")
    exit(0)
# 获取结果条目列表
translated = res_json['data']
# 依次输出
for item in translated:
    print(item['k'] + ': ' + item['v'])