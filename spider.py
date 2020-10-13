import bs4
import re
from urllib import request
import urllib
import xlwt
find_name=re.compile(r'<h2 class="champion_name">(.*?)</h2>')
find_title=re.compile(r'<h3 class="champion_title">(.*?)</h3>')
find_intro=re.compile(r'<p>(.*?)</p>')
find_tags=re.compile(r'<span class="champion_tooltip_tags">Tags:(.*?)</span>',re.S)
def main():
    baseurl="http://lol.qq.com/web200912/hero_list.htm"
    saveData(getData(askUrL(baseurl)))
def askUrL(baseurl):
    #header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    req=urllib.request.Request(url=baseurl)
    response=urllib.request.urlopen(req)
    html=""
    html=response.read().decode("ANSI")
    #这里的编码方式是ANSI
    return html;
def getData(html):
    bs=bs4.BeautifulSoup(html,"html.parser")
    info=bs.find_all("div",class_="cm_bg")
    #找到特征div块，获取其全部内容
    data=[]
    name=re.findall(find_name,str(info))
    #利用正则表达式搜索name，返回一个列表
    for each_name in name:
        data.append(each_name)
    title=re.findall(find_title,str(info))
    for each_title in title:
        data.append(each_title)
    intro=re.findall(find_intro,str(info))
    for each_intro in intro:
        data.append(each_intro)
    tag=re.findall(find_tags,str(info))
    for each_tag in tag:
        data.append(each_tag)

    return data
def saveData(data):
    workbook=xlwt.Workbook(encoding="utf-8")
    worksheet=workbook.add_sheet('sheet_1',cell_overwrite_ok=True)
    index=["英雄名","英雄称号","英雄介绍","英雄属性"]
    count=0
    for i in range(0,4):
        worksheet.write(0,i,index[i])
    for j in range(0,4):
        for i in range(1,41):
            worksheet.write(i,j,data[count])
            count+=1
    workbook.save("英雄概括.xls")



main()

