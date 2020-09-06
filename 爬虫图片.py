from urllib import request
import re

from pip._vendor import chardet

req = request.urlopen('https://coding.imooc.com/')
html = req.read()
encode_type = chardet.detect(html)
# A同学
html = html.decode(encode_type['encoding'])
img_urls = re.findall(r'src=.+\.jpg', html)

i = 0
for url in img_urls:
    url = str(url).replace("src=\"", "http:")
    # wb + 以二进制方式进行打开储存、图片需要以二进制方式打开存储
    f = open(str(i) + ".jpg", 'wb+')
    req = request.urlopen(url)
    img_file = req.read()
    f.write(img_file)
    i += 1
