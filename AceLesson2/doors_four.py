import random
#四門遊戲-三隻羊+一台車
print("【四門遊戲】")
#在還未開始之前，輸和贏都是0
win=0
lose=0

#TODO(6) 弄成迴圈，將次數增多，來計算贏和輸的機率
for times in range(1,100001,1):
    #TODO(1)洗牌-從三隻"羊"當中隨機插入一張有"車子"的牌
    #(類似洗鬼牌，將洗好的牌隨機插入鬼牌)
    cards=["羊","羊","羊"]
    cards.insert(random.randint(0,3),"車")
    # print("第",times,"迴圈",";","洗牌",cards)
    #TODO(2)男主角第一次抽籤
    R=random.randint(0,3)
    D=cards[R]
    # print("第一次抽出的籤號:",R,"；","男主角第一次開的門:",D)
    #TODO(3)男主角開的這個門是"車"，則顯示lose，並計算lose一次
    if D=="車":
        # 將男主角開的那台車移除
        # cards.remove(D)
        # print(cards)
        # print("結果:lose")
        #並計算一次lose
        lose+=1

    #TODO(4)男主角開的這個門是"羊"，則就要繼續判斷
    elif D=="羊":
        # 將男主角開的那隻羊移除
        del cards[R]
        # print("將男主角開的那隻羊移除",cards)
        # 主持人會將剩下的那隻羊刪除
        cards.remove("羊")
        # print("主持人會將剩下的那隻羊刪除",cards)
        #TODO(5)男主角再繼續抽第二次籤
        R = random.randint(0, 1)
        D=cards[R]
        # print("第二次抽出的籤號:",R,";","男主角第二次開的門:",D)
        # 男主角開的這個門是"車"，則顯示win，並計算win一次
        if D=="車":
            # print("結果:winner")
            win+=1
        # 男主角開的這個門是"羊"，則顯示lose，並計算lose一次
        elif D=='羊':
            # print("結果:lose")
            lose += 1

# TODO(7)計算輸和贏的機率
all=win+lose
print("抽籤次數",all)
print("贏的次數",win)
print("輸的次數",lose)
print("贏的機率",(win/all)*100,"%")
print("輸的機率",(lose/all)*100,"%")

print("======理論上======")
print("贏","3/4 * 1/2=",(3/4)*(1/2)*100,"%")
print("輸",(1-((3/4)*(1/2)))*100,"%")

print("======若不換牌======")
print("贏","1/4 =",(1/4)*100,"%")
print("輸",(3/4)*100,"%")


