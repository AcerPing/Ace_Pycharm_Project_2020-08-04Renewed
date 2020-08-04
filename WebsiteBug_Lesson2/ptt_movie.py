import requests
import warnings
warnings.filterwarnings("ignore") #隱藏"html.parser"警告
from bs4 import BeautifulSoup
from jieba.analyse import extract_tags

url = "https://www.ptt.cc/bbs/movie/M.1593936799.A.5E3.html"

#TODO:〔方法二〕使用requests來開啟url (會有預設的User-Agent)
response = requests.get(url)
# print(response.text)

'''
from urllib.request import urlopen,Request
#TODO:〔方法一〕若直接urlopen開啟會出現HTTP Error 403: Forbidden，所以要先附加header後再開啟
r = Request(url)
r.add_header("User-Agent","Mozilla/5.0")
response = urlopen(r)
'''

#以BeautifulSoup分析網頁
html = BeautifulSoup(response.text)
# print(html)
content = html.find(name="div",id="main-content",class_="bbs-screen bbs-content")
# print(content.text)

#TODO:用find尋找完之後，發現內容混砸，需要做分類以及篩選
metas = content.find_all(name="span",class_="article-meta-value")
print("作者:",metas[0].text)
print("看板:",metas[1].text)
print("標題:",metas[2].text)
print("時間:",metas[3].text)

#使用extract，將每一個去除
ms = content.find_all(name="div",class_="article-metaline") #作者、標題、時間
# print(ms)
for m in ms:
    # print(m)
    m.extract() #刪除作者、標題、時間
lookmovie = content.find(name="div",class_="article-metaline-right") #看板
# print(lookmovie)
lookmovie.extract() #刪除看板

#(個人練習)使用定義類別及函數(流程)
class Extract_all:
    def __init__(self,tag,carrer):
        self.comment=content.find_all(name=tag,class_=carrer)

    def extract(self):
        for c in self.comment:
            # print(m)
            c.extract()  # 刪除作者、標題、時間

C1=Extract_all(tag="div",carrer="push")
C1.extract
print(content.text)
#print(len(C1.comment)) #查看有幾則評論
keywords=extract_tags(content.text,10)
print("關鍵字:",keywords)







