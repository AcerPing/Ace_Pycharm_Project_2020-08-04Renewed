from urllib.request import urlopen
import json
import codecs
url="https://www.google.com/doodles/json/2020/3?hl=zh_TW" #先從Google開發人員工具中複製貼上Request URL
response=urlopen(url) #以urlopen打開網頁
# print(response.read()) #發現讀取的檔案是b'的原始檔案型式
# print(json.load(response)) #以json.load做整理，呈現出[]list及{}字典的型式
doodles=json.load(response) #List
for x in doodles: #字典dictionary
    URL="https:" + x["url"]
    print(x["title"],URL)

    #TODO:針對圖片做處理 (記得縮排!!!)
    #縮排→每個字串都走過一遍
    #沒有做縮排→x只會是最後的值
    Response=urlopen(URL) #以urlopen打開圖片的網頁
    # print(Response.read()) #讀取檔案
    Image=Response.read()
    # print(URL.split("/")[-1]) #字串切割成串列+取最後的圖片檔名
    Name="doodles/"+URL.split("/")[-1] #儲存位置
    with codecs.open(Name,mode="wb") as file:
        file.write(Image)

