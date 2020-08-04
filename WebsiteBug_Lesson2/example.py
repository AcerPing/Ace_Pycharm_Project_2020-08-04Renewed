import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

NONCE = "bd1d47b37f"
# PD
datas = {
    "title":[],
    "url":[]
}
url = "https://buzzorange.com/wp-admin/admin-ajax.php"
for i in range(10):
    print("頁數:", i+1)
    params = {
        "action": "fm_ajax_load_more",
        "nonce": NONCE,
        "page": str(i+1)
    }
    response = requests.post(url, data=params)
    # print(response.text)
    p = json.loads(response.text)
    if "data" in p:
        html = BeautifulSoup(p["data"])
        for title in html.find_all("h4", class_="entry-title"):
            a = title.find("a")
            print(a.text)
            print(a["href"])
            print("-" * 50)
            # PD
            datas["title"].append(a.text)
            datas["url"].append(a["href"])
    else:
        print("已經沒了")
        break
# PD
df = pd.DataFrame(datas, columns=["title", "url"])
df.to_csv("buzz.csv", encoding="utf-8", index=False)