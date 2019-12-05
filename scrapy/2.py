import urllib.request

import re



url = 'https://movie.douban.com/top250'
request = urllib.request.Request(url)

request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
response = urllib.request.urlopen(request)

buf = response.read()


buf = str(buf, encoding='utf-8')

print(re, "____")

listurl = re.findall(r'http.+\.jpg', buf)

fo = open("1.js", 'w', encoding='utf-8')
fo.write("list="+str(listurl))
fo.close()

i = 1
for url in listurl:
    f = open("a" + str(i)+'.jpg', 'wb+')
    req = urllib.request.urlopen(url)
    buf = req.read()
    f.write(buf)
    i += 1
print(listurl)
