'''
from pytube import Playlist
playlist = "https://www.youtube.com/watch?v=wdH26D8Ssww&list=PLg_r40S5jeMIvAaq9OZweLCx8_N1OxO_Q" #欲下載清單
pl = Playlist(playlist)
pl.download_all()
print('下載完成！')
'''

'''
from pytube import Playlist
playlist = Playlist("https://www.youtube.com/playlist?list=PLynhp4cZEpTbRs_PYISQ8v_uwO0_mDg_X")
for video in playlist:
    print(video)
    video.streams.get_highest_resolution().download()
'''
'''
from pytube import YouTube

def yt(URL,path):
    yt = YouTube(URL)
    (yt.streams
     .filter(progressive=True, file_extension='mp4')
     .order_by('resolution')[-1]
     .download(path))

yt("https://www.youtube.com/watch?v=a20uIGxPgeA","D:/Python_Summarize/PycharmProjects/WebsiteBug_Lesson2/YT")

'''
for i in range(10,-1,-1):
    print(i,end=",")