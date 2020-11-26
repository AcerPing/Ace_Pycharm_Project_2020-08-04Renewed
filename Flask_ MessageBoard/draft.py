import pymysql

def post():
    global page
    try:
        page = int(input("請輸入頁數"))
    except:
        page = 0

    return "None",page

def load_data():
    conn = pymysql.connect(host="localhost", user="root", db="block", charset="utf8", port=None)
    cur = conn.cursor()  # 取得指令操作變數
    page = post()
    try:
        # print(post())
        # cur.execute("SELECT * FROM `article` LIMIT 5*(page+1) OFFSET 5*page")
        # cur.execute("SELECT * FROM `article` LIMIT 5*(%s+1) OFFSET 5*%s", [page,page])
        offset = 5 * page
        LIMIT = 5 * (page + 1)
        seq = "SELECT * FROM `article` LIMIT {LIMIT} OFFSET {offset}".format(LIMIT=LIMIT,offset=offset)
        cur.execute(seq)
        # cur.execute("SELECT * FROM `article` LIMIT 5*({page}+1) OFFSET 5*{page}".format(page=page))
    except:
        cur.execute("SELECT * FROM `article` LIMIT 5 OFFSET 0")
    finally:
        list = cur.fetchall()
        conn.commit()
        conn.close()
        print(list)

load_data()

page = post()
print(post()[1])
offset = 5*page
LIMIT = 5*(page+1)
print("SELECT * FROM `article` LIMIT {LIMIT} OFFSET {offset}".format(LIMIT=LIMIT,offset=offset))


