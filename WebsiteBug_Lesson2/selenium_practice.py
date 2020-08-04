from selenium.webdriver import Chrome
import time
from pytube import YouTube
from pytube import Playlist
import os

#TODO:定義pytube套件的下載函式，方便之後可以呼叫
def yt(URL,path):
    yt = YouTube(URL)
    (yt.streams
     .filter(progressive=True, file_extension='mp4')
     .order_by('resolution')[-1]
     .download(path))

#TODO:利用selenium的Chrome套件開啟Google帳號
driver = Chrome("./chromedriver")
#打開網址
driver.get("https://www.youtube.com/view_all_playlists")
#find → find_element
#find_all → find_elements
driver.find_element_by_id("identifierId").send_keys("410134003@gms.ndhu.edu.tw") #輸入帳號
driver.find_element_by_id("identifierNext").click() #點擊『繼續』
time.sleep(10) #等待
driver.find_element_by_class_name("whsOnd").send_keys("njla0301") #輸入密碼
driver.find_element_by_id("passwordNext").click() #點擊『繼續』
time.sleep(10)

#TODO:利用pytube下載youtube的playlist影片
#播放清單中有一支以上的影片
ps = driver.find_elements_by_class_name("vm-video-title-text")
for p in ps:
    #bs4 .text → .text
    title = p.text
    # print(title)
    #bs4 ["href"] → get_attribute("href")
    url = p.get_attribute("href")
    print(title,url)

    playlist = Playlist(url)
    for video in playlist:
        print(video)

        dirname = "YT/" + title + "/"  # 依照月份分類必須先建資料夾
        if not os.path.exists(dirname):  # 判斷檔案是否存在：如果檔案是不存在的，則建立資料夾
            os.mkdir(dirname)

        yt(video,path=dirname)

print("download_all")

time.sleep(10)
driver.close() #關閉瀏覽器


