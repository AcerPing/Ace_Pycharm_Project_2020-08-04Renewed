from random import randint

paper=0  #令period為買彩券的期數，還沒開始購買之前是0期

#TODO(5)四次開出的彩券，每次當期中獎的號碼有四個以上，才停止購買(跳出迴圈)
for period in range(1,5,1):

    #TODO(2)官網開出彩券
    #開出的號碼不重複、都是號碼(同類型)、沒有順序性→使用set
    award=set() #當尚未開獎之前，為一組空set，叫做award;每跑一次迴圈，就要歸零重新計算
    while len(award)<7: #當award的set的長度小於7時，執行迴圈;直到有7個數字加入到award的set中才跳出迴圈
        award.add(randint(1,48)) #從1到48號中隨機抽取數字到award的set中
          
    # TODO(4)當期中獎的號碼在四個以下時，執行迴圈，直到有四個以上的號碼中獎時，才跳出此迴圈
    while True:
        #TODO(1)我買的彩券
        #開出的號碼不重複、都是號碼(同類型)、沒有順序性→使用set
        lottery=set() #當尚未購買之前，為一組空set，叫做lottery;每跑一次迴圈，就要歸零重新計算
        while len(lottery)<7: #當lottery的set的長度小於7時，執行迴圈;直到有7個數字加入到lottery的set中才跳出迴圈
            lottery.add(randint(1,48)) #從1到48號中隨機抽取數字到lottery的set中

        paper += 1  #每一次輪迴，算購買一張彩券

        #TODO(3)從我買的彩券中，一個一個檢視號碼，是否有在官網開出彩券當中
        t=0 #中了幾個號碼，尚未核對之前為0，每跑一次迴圈，就要歸零重新計算
        y=[] #我買的彩券中，哪幾個號碼中獎，尚未核對之前為空，每跑一次迴圈，就要歸零重新計算
        for x in lottery: #從我買的彩券中，一個一個檢視號碼
            if x in award: #如果有在官網開出彩券當中
                y.append(x) #如果我買的彩券中，這個號碼有中獎，則加入y字串中
                t+=1 #並算一次中獎次數
        
        # TODO(6-1)總結-每張購買的彩券細項
        # print("第幾期:", period,';',"購買第幾張彩券:", paper)  # 購買彩券的期數
        # print("award:", award)  # 當期官網開出彩券中，
        # print("lottery:", lottery)  # 期官網開出彩券中，中了兩個號碼的我買的彩券
        # print("中獎的字串:", y)  # 哪幾個號碼中獎
        # print("中了幾個號碼:", t)  # 中了幾個號碼
        # print(" ") #排版

        if t>=4: #核對完之後，若中獎的數字有四個以上則結束迴圈
            break
        else: #否則繼續迴圈
            continue

    # # TODO(6-2)總結-當我購買的彩券有中到四個數字時細項
    print("第幾期:", period,';',"購買第幾張彩券:", paper)  # 購買彩券的期數
    print("award:", award)  # 當期官網開出彩券中，
    print("lottery:", lottery)  # 期官網開出彩券中，中了兩個號碼的我買的彩券
    print("中獎的字串:", y)  # 哪幾個號碼中獎
    print("中了幾個號碼:", t)  # 中了幾個號碼
    print(" ")

#TODO(6-3)總共買了幾張
print("總共買了幾張",paper)
# print("總共買了幾期",period)












