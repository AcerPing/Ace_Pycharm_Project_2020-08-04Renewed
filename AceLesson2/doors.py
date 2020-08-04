#三門遊戲-兩隻羊+一台車
print("【三門遊戲】")
#在還未開始之前，輸和贏都是0
win=0
lose=0
#TODO(4) 弄成迴圈，將次數增多，去計算贏和輸的機率
for times in range(1,100000,1):
#TODO(1)洗牌-隨機插入一張有"車子"的牌
#(類似洗鬼牌，將洗好的牌隨機插入鬼牌)
    import random
    cards=["羊","羊"]
    cards.insert(random.randint(0,2),"車")
    # print(cards)
    #TODO(2)男主角隨機開一個門，而這個門是"車"
    #男主角隨機開一個門
    D=cards[random.randint(0,2)]
    #男主角開的這個門是"車"，則顯示lose
    if D=="車":
        # print("男主角開的門",D)
        # print("lose")
        lose+=1

    #TODO(3)男主角隨機開一個門，而這個門是"羊"
    #男主角開的這個門是"羊"
    #主持人會將剩下的那隻羊刪除
    elif D=="羊":
        # print("男主角開的門",D)
        # print("winner")
        win+=1

#計算輸和贏的機率
all=win+lose
print("贏的次數",win)
print("輸的次數",lose)
print("贏的機率",(win/all)*100,"%")
print("輸的機率",(lose/all)*100,"%")

print("======理論上======")
print("贏","2/3=",(2/3)*100,"%")
print("輸","1/3",(1/3)*100,"%")

print("======若不換牌======")
print("贏","1/3 =",(1/3)*100,"%")
print("輸","2/3 =",(2/3)*100,"%")



