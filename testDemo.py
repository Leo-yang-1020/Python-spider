import requests

# r=requests.get("http://lol.qq.com/web200912/hero_list.htm");
# print(r.text.encode("GB2312"))
# # with open("r.txt",mode='w',encoding="utf-8") as f:
# #     f.writelines(r.text)
import requests

r = requests.get('http://lol.qq.com/web200912/hero_list.htm')

print (type(r))

print (r.encoding)

print (r.apparent_encoding)

print ((r.text.encode(r.encoding).decode(r.apparent_encoding)))