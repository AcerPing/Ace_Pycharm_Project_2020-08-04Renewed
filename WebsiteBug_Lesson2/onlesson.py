from urllib.request import urlopen,Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import warnings

url="https://www.google.com/search?q=tibame&sxsrf=ALeKk02QqH8Oyy2ARxf3yNyPkPU455SPxw:1593487292527&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiis5ngyqjqAhVBGaYKHV-WCosQ_AUoAXoECAwQAw&biw=1530&bih=663&dpr=1.25"

#TODO:披著羊皮進入服務台索要資料
request = Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})

#TODO:以urlopen開啟檔案
with urlopen(request) as file:
    data = file.read().decode("utf8")
# print(data)

#解析網頁原始碼
warnings.filterwarnings("ignore")
html=BeautifulSoup(data) #網頁→beautifulsoup4分析工具
# print(html)
# print()
# print("現在處理的頁面", page, ";", "及url:", url)
# print()

#TODO: find(找第一個符合條件的) ; find_all(找所有符合條件的)
#TODO: find答案:1個 ; find_all:List
#TODO: print(html.find_all("li",{"class":"list-rst"})) #第一種寫法
for news in html.find_all("div",class_="gG0TJc"): #TODO:第二種寫法
    title=news.find("a",class_="l lLrAF")
    # source=news.find("span",class_="xQ82C e8fRJf")
    # date = news.find_all("span", class_="f nsa fwzPFf")
    print(title.text)
    # print(title.text,title["href"],source.text,date.text)

