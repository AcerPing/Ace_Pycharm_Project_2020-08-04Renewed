from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=["日文名","英文名","跳轉","評分"]) #預先準備DataFrame

page=59
while True: #一直從第一頁搜尋到最後一頁，但不知道最後一頁是第幾頁，所以採用無限迴圈
    url="https://tabelog.com/tw/tokyo/rstLst/"+str(page)+"/?SrtT=rt" #食べログのアドレス
    #事後解決
    try:
        response=urlopen(url) #以url開啟網址
    except HTTPError: #當發生HTTPError錯誤時，則跳到下方
        print()
        print("最後一頁了")
        print()
        break #跳出迴圈
    html=BeautifulSoup(response) #網頁→beautifulsoup4分析工具
    # print(html)
    print()
    print("現在處理的頁面", page, ";", "及url:", url)
    print()

    #TODO: find(找第一個符合條件的) ; find_all(找所有符合條件的)
    #TODO: find答案:1個 ; find_all:List
    #TODO: print(html.find_all("li",{"class":"list-rst"})) #第一種寫法
    for restaurant in html.find_all("li",class_="list-rst"): #TODO:第二種寫法
        japan=restaurant.find("small",class_="list-rst__name-ja")
        english=restaurant.find("a",class_="list-rst__name-main js-detail-anchor")
        score = restaurant.find_all("b", class_="c-rating__val")
        print(japan.text,
              english.text,
              english["href"],
              score[0].text,) #萃取紙條(.text) #萃取特別特徵([href])

        series = pd.Series([japan.text,english.text,english["href"],score[0].text],index=["日文名","英文名","跳轉","評分"])
        #將每筆資料變成Series
        df = df.append(series,ignore_index=True) #加入到DataFrame

    #TODO:打開→分析→到下一頁
    page=page+1

#存檔
df.to_csv("tabelog.csv",encoding="utf-8",index=False)