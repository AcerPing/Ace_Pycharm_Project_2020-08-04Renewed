from app.routes import app
# from app import app

#啟動網站伺服器，可透過port參數指定埠號
if __name__=="__main__": #如果以主程式執行
    app.run(debug=True) #立刻啟動伺服器