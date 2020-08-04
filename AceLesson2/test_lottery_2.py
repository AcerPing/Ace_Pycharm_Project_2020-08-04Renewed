from random import randint

period=0 #令period為買彩券的期數，還沒開始購買之前是0期
t=0 #令t為中了幾個號碼，還未對獎之前是0個號碼

#TODO(4)當期開出的彩券，都只買一張，直到中獎的號碼有四個以上，才停止購買，請問需要買幾期?
while t<4:
    #TODO(2)官網開出彩券
    # 開出的號碼不重複、都是號碼(同類型)、沒有順序性→使用set
    award=set() #當尚未開獎之前，為一組空set，叫做award;每跑一次迴圈，就要歸零重新計算
    while len(award)<7: #當award的set的長度小於7時，執行迴圈;直到有7個數字加入到award的set中才跳出迴圈
        award.add(randint(1,48)) #從1到48號中隨機抽取數字到award的set中

    #TODO(1)我買的彩券
    #開出的號碼不重複、都是號碼(同類型)、沒有順序性→使用set
    lottery=set() #當尚未購買之前，為一組空set，叫做lottery;每跑一次迴圈，就要歸零重新計算
    while len(lottery)<7: #當lottery的set的長度小於7時，執行迴圈;直到有7個數字加入到lottery的set中才跳出迴圈
        lottery.add(randint(1,48)) #從1到48號中隨機抽取數字到lottery的set中

    #TODO(3)從我買的彩券中，一個一個檢視號碼，是否有在官網開出彩券當中
    t=0 #中了幾個號碼，每跑一次迴圈，就要歸零重新計算
    y=[] #我買的彩券中，哪幾個號碼中獎，每跑一次迴圈，就要歸零重新計算
    for x in lottery: #從我買的彩券中，一個一個檢視號碼
        if x in award: #如果有在官網開出彩券當中
            y.append(x) #如果我買的彩券中，這個號碼有中獎，則加入y字串中
            t+=1 #並算一次中獎次數

    period += 1  # 每一次輪迴，都算是購買一期彩券

#TODO(5)總結
print("award:",award) #當期官網開出彩券的號碼
print("lottery:",lottery) #當期我買的彩券號碼
print("中獎的字串:",y)  #哪幾個號碼中獎
print("中了幾個號碼:",t) #中了幾個號碼
print("購買彩券的期數",period) #購買彩券的期數






