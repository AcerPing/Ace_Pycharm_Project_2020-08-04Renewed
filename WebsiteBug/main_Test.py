from urllib.request import urlopen,urlretrieve
import json
import os
import codecs

for m in range(1,7,1):
    url="https://www.google.com/doodles/json/2020/"+str(m)+"?hl=zh_TW" #Request URL
    print()
    print("現在處理進度:",url)
    print()
    response=urlopen(url)
    # print(response.read()) #b'檔案原始碼
    Jason=json.load(response) #list+dict

    for x in Jason:
        URL="https:"+x['url']
        print(x['title'],URL)

        #針對圖面做處理
        Response=urlopen(URL)
        IMG=Response.read()

        #需事先建立資料夾，才能儲存檔案
        if os.path.exists("doodles\\"+str(m)+"\\")==False: #如果判斷這個路徑底下的檔案不存在(False)，則建立資料夾
            os.mkdir("doodles\\"+str(m))

        #儲存圖片至資料夾"doodles\\"底下
        FileName="doodles\\"+str(m)+"\\"+URL.split("/")[-1] #路徑+檔名
        # print(FileName)
        urlretrieve(url=URL,filename=FileName) #並將圖片儲存到這個資料夾底下




    # with codecs.open(filename=FileName,mode="wb") as file:
    #     file.write(IMG)
