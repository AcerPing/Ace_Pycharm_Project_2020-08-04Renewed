from urllib.request import urlopen,urlretrieve
import json
import os

for month in range(0,6,1):
    url="https://www.google.com/doodles/json/2020/"+str(month+1)+"?hl=zh_TW" #先從Google開發人員工具中複製貼上Request URL，中間表示月份(1-6)
    print("現在處理的頁面:", url)

    response=urlopen(url) #以urlopen打開網頁
    # print(response.read()) #發現讀取的檔案是b'的原始檔案型式
    # print(json.load(response)) #以json.load做整理，呈現出[]list及{}字典的型式
    doodles=json.load(response) #List

    for x in doodles: #字典dictionary
        URL="https:" + x["url"]
        print(x["title"],URL)

        dirname="doodles/" + str(month + 1) + "/" #依照月份分類必須先建資料夾
        if not os.path.exists(dirname): #判斷檔案是否存在：如果檔案是不存在的，則建立資料夾
            os.mkdir(dirname)

        #TODO:針對圖片做處理 (記得縮排!!!)
        #TODO:縮排→每個字串都走過一遍
        #沒有做縮排→x只會是最後的值
        # print(URL.split("/")[-1]) #字串切割成串列+取最後的圖片檔名
        Name=dirname+URL.split("/")[-1] #儲存位置
        urlretrieve(URL,Name) #利用urlretrieve下載檔案


