# import sys
# print(sys.argv[1])

# import os
# import time
# os.system("tasklist")
# time.sleep(10)
# os.system("cls")

#引言
import sys
import webbrowser
import time
import os

#顯示sys.argv的字串長度
print(len(sys.argv))

#當sys.argv的字串長度小於2時，也就是沒有打網址，則顯示"out of range"，並在2秒後清除(cls)
if len(sys.argv)<2:
    print("out of range")

#其他(當sys.argv的字串長度不小於2時)，則先顯示網址，並跳賺到網址
else:
    print(sys.argv[1])
    webbrowser.open(sys.argv[1])

#2秒後清除(cls)
time.sleep(5)
os.system("cls")
