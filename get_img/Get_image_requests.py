#python3.4
import re, requests
 
r = requests.get("http://fashion.qq.com/visual/photo.shtml")
p = re.compile('src="(.+?\.jpg)"')
image = p.findall(r.text)
x=1
for item in image:
    try:
        img_get = requests.get(item.strip())
        name=str(x)+'.jpg'
        sz = open(name, 'wb').write(img_get.content)
        x=x+1
    except:
        print(x,item)
        x=x+1
        continue
