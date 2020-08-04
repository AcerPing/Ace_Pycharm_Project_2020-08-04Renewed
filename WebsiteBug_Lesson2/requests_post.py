import requests
import json
import warnings
warnings.filterwarnings("ignore")
import codecs
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=["title", "URL"]) #預先準備DataFrame

url = "https://buzzorange.com/wp-admin/admin-ajax.php"

for page in range(0,10,1): #處理頁面範圍
    print("\n")
    print("現在處理的頁面", page+1)

    NONCE = "8df07c7806"  # nonce要每天填
    D = {"action":"fm_ajax_load_more","nonce":NONCE,"page":str(page+1)}
    response = requests.post(url,data=D)

    #內容→.text
    print(response.text) #字典形式

    #'str' object has no attribute 'read'
    #TODO:文字→json.loads
    #檔案→json.load
    news = json.loads(response.text) # print(news) #字典形式

    # with codecs.open("buzz.html","w",encoding="utf-8") as file: #寫入news字典形式內容，讓firefox做後續解讀
    #     file.write(str(news))

    #TODO:先判斷該網頁是否有資料(data)
    #print(news.keys())
    if 'data' in news.keys(): #如果有資料(data)的話，則用BeautifulSoup分析網頁
        html = BeautifulSoup(news['data'])
        # print(html) #網頁原始碼形式
        for title in html.find_all(name="h4",class_="entry-title"): #尋找每一個h4標籤的class_="entry-title"的tag，list形式
            # print(title)
            a = title.find("a")
            print(a.text) #新聞標題文字
             #尋找超連結標籤
            print(a["href"]) #顯示超連結
            print("-"*50) #排版

            series = pd.Series([a.text, a["href"]],index=["title", "URL"]) #將每筆資料變成Series
            df = df.append(series, ignore_index=True)  # 加入到DataFrame

    else: #如果沒有資料(data)的話，則顯示"已經沒了"並跳出迴圈
        print("已經沒了")
        break

df.to_csv("buzzorange.csv", encoding="utf-8", index=False) #存檔



