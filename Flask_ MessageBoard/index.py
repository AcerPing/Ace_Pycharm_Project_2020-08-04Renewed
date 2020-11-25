#encoding = uft-8
from flask import Flask,render_template,request,redirect,escape,Markup
from datetime import datetime

#引入MySQL
import pymysql
# import MySQLdb

#申請空間
app = Flask(__name__)
#127.0.0.1:5000

@app.route('/')
def hello():
    list = load_data()
    print(list)
    #顯示MySQL DataBase完整資訊，方便修正
    return render_template("index.html",list=list)

#方法
@app.route("/post", methods=['GET','POST'])
def post():

    #方法一
    name = request.args.get("name","匿名")
    name = name.replace('',"匿名（隠し子）")
    comment = request.args.get("comment","暫無留言")
    comment = comment.replace('',"暫無留言（無し）")

    #方法二
    # name = request.values.get("name","匿名")
    # comment = request.values.get("comment","暫無留言")
    delete_number = request.values.get("delete_number", None)
    modified_number = request.values.get("modified_number", None)
    modified_name = request.values.get("modified_name", None)
    modified_comment = request.values.get("modified_comment", None)

    #方法三
    # name = request.form.get("name","匿名")
    # comment = request.form.get("comment","暫無留言")

    create_time = datetime.now()

    # 顯示資訊，方便修正
    # print(repr(modified_number))
    # print(repr(delete_number))

    if delete_number != None and delete_number !='':
        delete_message(delete_number)
    elif modified_number != None and modified_number !='':
        change_message(modified_number, modified_name, modified_comment)
    else:
        save_time(name, comment, create_time)

    return redirect('/')

def save_time(name,comment,create_time):
    #連接數據庫MySQL
    conn = pymysql.connect(host="localhost",user="root",db="block",charset="utf8",port=None)
    cur = conn.cursor() #取得指令操作變數
    #執行插入方法，入的SQL語句
    #格式化的作用是為了防止SQL注入，`的作用是為了防止關鍵詞被數據庫解析
    cur.execute("INSERT INTO `article`(`name`,`comment`,`create_time`) VALUES(%s,%s,%s)",[name,comment,create_time])
    conn.commit()
    conn.close()

def delete_message(delete_number):
    # print(repr(delete_number)) #顯示delete_number資訊，方便修正
    #連接數據庫MySQL
    conn = pymysql.connect(host="localhost",user="root",db="block",charset="utf8",port=None)
    cur = conn.cursor() #取得指令操作變數
    #執行插入方法，入的SQL語句
    #格式化的作用是為了防止SQL注入，`的作用是為了防止關鍵詞被數據庫解析
    cur.execute("DELETE FROM `article` WHERE `id`=%s",[delete_number])
    conn.commit()
    conn.close()

def change_message(modified_number,modified_name,modified_comment):
    print(repr(modified_number)) #顯示delete_number資訊，方便修正
    #連接數據庫MySQL
    conn = pymysql.connect(host="localhost",user="root",db="block",charset="utf8",port=None)
    cur = conn.cursor() #取得指令操作變數
    #執行插入方法，入的SQL語句
    #格式化的作用是為了防止SQL注入，`的作用是為了防止關鍵詞被數據庫解析
    cur.execute("UPDATE `article` SET `name`=%s,`comment`=%s WHERE `id`=%s", [modified_name,modified_comment,modified_number])
    conn.commit()
    conn.close()

def load_data():
    conn = pymysql.connect(host="localhost", user="root", db="block", charset="utf8", port=None)
    cur = conn.cursor() #取得指令操作變數
    cur.execute("SELECT * FROM `article`")
    list = cur.fetchall()
    conn.commit()
    conn.close()
    return list

#使datetime對象更容易分辨的模板的過濾器
@app.template_filter("datetime_fmt")
def datetime_filter(dt):
    return dt.strftime(str('%Y/%m/%d %H:%M:%S'))

#將換行符置換為br標籤的模板過濾器
@app.template_filter("nl2br")
def nl2br(s):
    return escape(s).replace("\\n",Markup('<br>'))

# 伺服器啟動，執行flask項目
if __name__ == "__main__":
    app.run()
# host = "0.0.0.0"