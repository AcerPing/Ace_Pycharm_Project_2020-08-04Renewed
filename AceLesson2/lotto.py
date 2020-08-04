import random
#TODO:官網開出的彩券
#設一個空集合，叫做prize
prize=set()
#抽出號碼直到prize有七個不重複的數字
while len(prize)<7:
    # 隨機抽號加入prize的set中
    n=random.randint(1,48)
    prize.add(n)
print("官方開出的彩券:",prize)

#(利用while迴圈)一期開出，買樂透直到中了四個數字以上為止，並計算我買了幾張樂透
#重點
#(1)無窮迴圈+手動停止(break)
#(2)使用時機:當while條件寫不出來的時候
paper=0
while True:
    #TODO:我買的彩券
    #設一個空集合，叫做lotto
    lotto=set()
    #同時記錄次數，起始值為0
    # time=0
    #抽出號碼直到lotto有七個不重複的數字
    while len(lotto)<7:
    #隨機抽號加入lotto的set中
        N=random.randint(1,48)
        lotto.add(N)
        # time+=1
    print("我買的彩券",lotto)
    # print("次數:",time)

    #計算買了幾張
    paper+=1

    #檢視我買的彩券中，中了幾個號碼
    t=0
    #買的彩券中，一個號碼一個號碼檢視，中了幾個號碼
    for x in lotto:
        if x in prize:
            print(x,"中籤")
            t+=1
    #全部號碼檢視完畢之後，再去計算中個幾個數字
    print("中了幾個數字",t)

    #當我中了四個以上的數字時，就跳出迴圈
    if t>=4:
        break

print("買了幾張:",paper)

# if lotto==prize:
#     print("中樂透")
# else:
#     print("繼續加油")

