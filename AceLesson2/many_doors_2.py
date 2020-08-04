#多門遊戲-多隻羊+一台車
print("【多門遊戲，但直到贏為止】")

from random import randint

#在還未開始之前，輸和贏都是0
win=0
lose=0

#TODO(6) 弄成迴圈，固定次數，將次數增多，來計算贏和輸的機率
while True:
    #TODO(1)洗牌-洗牌-從很多羊當中插入一台車
    cards=[] #先令cards為一組空的字串
    cards=["羊"]*10000#插入多隻羊
    # print(cards) #check
    cards.insert(randint(0,len(cards)),"車") #再插入一台車
    # print("第",times,"迴圈",";","洗牌",cards)
    #TODO(2)男主角第一次抽籤
    R=randint(0,len(cards)-1) #隨機抽一個號碼
    D=cards[R] #這個號碼在這組字串中代表??
    # print("第一次抽出的籤號:",R,"；","男主角第一次開的門:",D) #check
    #TODO(3)男主角開的這個門是"車"，則顯示lose，並計算lose一次
    if D=="車":
        lose+=1
        continue

    #TODO(4)男主角開的這個門是"羊"，則就要繼續判斷
    elif D=="羊":
        del cards[R] # 將男主角開的那隻羊移除
        cards.remove("羊") # 主持人會將剩下的那隻羊刪除
        # print("第二次抽籤",cards) #check
        #TODO(5)男主角再繼續抽第二次籤
        R = randint(0, len(cards)-1) #隨機再抽一個號碼
        D=cards[R] #這個號碼在這組字串中代表??
        # print("第二次抽出的籤號:",R,";","男主角第二次開的門:",D)
        # 男主角開的這個門是"車"，則顯示win，並計算win一次
        if D=='羊':
            lose += 1
            continue
        # 男主角開的這個門是"羊"，則顯示lose，並計算lose一次
        elif D=="車":
            win+=1
            break

# TODO(7)計算輸和贏的機率
all=win+lose
print("抽籤次數",all)
print("贏的次數",win)
print("輸的次數",lose)
print("贏的機率",(win/all)*100,"%")
print("輸的機率",(lose/all)*100,"%")

print("======若不換牌的機率======")
print("(贏)要抽中車:",((1/(10000+1))*100),"%")
print("(輸)抽中羊:",(1-(1/(10000+1)))*100,"%")



