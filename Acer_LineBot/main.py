#啟動flask
#flask starter example

from flask import Flask
app = Flask(__name__) #__name__代表目前執行的模組

#準備一個路徑口(URN)
#此路徑為/
#用戶訪問此路徑的時候，回傳Hello, World!

@app.route('/') #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def hello_world():
    return 'Hello, World!'

#準備一個路徑口(URN)
#此路徑為lbh
#用戶訪問此路徑的時候，回傳hahaha

@app.route('/lbh') #根目錄，代表我們要處理的網站路徑
def hello_lbh():
    return 'hahaha'

#準備一個路徑口(URN)
#此路徑為simulate-ai
#用戶訪問此路徑的時候，執行1+1，並回傳數值

@app.route('/simulate-ai')
def simulate_ai():
    calresult=1+1
    return str(calresult)

#準備一個路徑口(URN)
#此路徑為return-html
#用戶訪問此路徑的時候，回傳一個網頁

@app.route('/return-html')
def return_html():
    return "<h1>dasdad<h1>"

#準備一個路徑口(URN)
#此路徑為fake-html
#用戶訪問此路徑的時候，用request模組去訪問網頁
#request get some website example
# 把該網頁的文字回傳

import requests
@app.route('/fake-html')
def fake_html():
    CrawlerResult=requests.get("https://www.toutiao.com/ch/news_tech/")
    return CrawlerResult.text

app.run() #啟動伺服器