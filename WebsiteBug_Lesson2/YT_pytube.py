from pytube import YouTube

yt = YouTube('https://youtu.be/9bZkp7q19f0') #想下載的影片連結
# print(yt.title)


#Quick start -1
YouTube('https://www.youtube.com/watch?time_continue=279&v=6GQr7mR4FfA&feature=emb_logo').streams.get_highest_resolution().download() #下載影片


'''
#Quick start -2
(yt.streams
.filter(progressive=True, file_extension='mp4')
.order_by('resolution')[-1]
.download())
# print(yt.streams)
'''

'''
#Usage
YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[0].download()
'''











