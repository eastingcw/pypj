#python3.4
import urllib.request
import re
 
def getHtml(url):
    page = urllib.request.urlopen(url)
    #decode('utf-8')编码有时不同
    html = page.read().decode('gbk')
    return html
 
def getImg(html):
    reg = 'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x+=1
        print(x)
 
html = getHtml("http://fashion.qq.com/visual/photo.shtml")
 
getImg(html)
 
