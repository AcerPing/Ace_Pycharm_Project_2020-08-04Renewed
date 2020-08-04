# time=0
# while time<3:
#     me=input("請猜拳:[0]剪刀,[1]石頭,[2]布\n")
#     me=int(me)
#     import random
#     pc=random.randint(0,2)
#     transfer=["剪刀","石頭","布"]
#     print("你出的拳:",transfer[me])
#     print("機器人出的拳",transfer[pc])
#     if pc==(me+1)%3:
#         print("lose")
#     elif pc==me:
#         print("equal")
#     else:
#         print("win")
#     time+=1

# for time in range(0,3):
#     me=input("請猜拳:[0]剪刀,[1]石頭,[2]布\n")
#     me=int(me)
#     import random
#     pc=random.randint(0,2)
#     transfer=["剪刀","石頭","布"]
#     print("你出的拳:",transfer[me])
#     print("機器人出的拳",transfer[pc])
#     if pc==(me+1)%3:
#         print("lose")
#     elif pc==me:
#         print("equal")
#     else:
#         print("win")

#TODO(6)用成迴圈
result=[]
lose=0
# equal=0
win=0
time=0
while time<3:

    #TODO(1)列出剪刀石頭布的文字list
    transfer=["剪刀","石頭","布"]

    #TODO(2)我出拳
    me=input("請猜拳:[0]剪刀,[1]石頭,[2]布\n")
    #將我輸入的文字轉成數字
    me=int(me)

    #TODO(3)換機器人猜拳
    #機器人隨機出拳
    import random
    pc=random.randint(0,2)

    #TODO(4)顯示雙方出的拳
    print("你出的拳:",transfer[me])
    print("機器人出的拳",transfer[pc])

    #TODO(5)判斷輸贏
    #如果我出的拳的數字+1會是機器人出的拳的數字，則會輸
    if pc==(me+1)%3:
        print("lose")
        result=result+["lose"]
        lose+=1

    #如果我出的拳的數字等於機器人出的拳的數字，則平手
    elif pc==me:
        print("equal")
        result = result + ["equal"]
        # equal+=1
        time=time-1

    #其他的結果只剩下贏
    else:
        print("win")
        result = result + ["win"]
        win+=1

    time+=1

#TODO(7)總結三次猜拳的結果
#顯示三次猜拳的結果
print(result)
#判斷三次猜拳的勝負
if lose>=2:
    print("敗")
# elif equal>=2:
#     print("平手")
elif win>=2:
    print("勝")
