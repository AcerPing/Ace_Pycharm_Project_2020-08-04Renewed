from random import randint

#TODO(2)官網開出彩券
#開出的號碼不重複、都是號碼(同類型)、沒有順序性→使用set
award=set() #設定一個空set，叫做award
while len(award)<7: #當award的set的長度小於7時，執行迴圈;直到有7個數字加入到award的set中才跳出迴圈
    award.add(randint(1,48)) #從1到48號中隨機抽取數字到award的set中
# print(award) #check
# print("長度:",len(award)) #check

#TODO(4)當期的彩券開出後，一直買一直買，直到中了四個號，才停止(跳出迴圈)
paper=0 #另paper為買彩券的張數，起始值為0張
t=0 #另t為中了幾個號碼
while t<4:
    #TODO(1)我買的彩券
    #開出的號碼不重複、都是號碼(同類型)、沒有順序性→使用set
    lottery=set() #設定一個空set，叫做lottery
    while len(lottery)<7: #當lottery的set的長度小於7時，執行迴圈;直到有7個數字加入到lottery的set中才跳出迴圈
        lottery.add(randint(1,48)) #從1到48號中隨機抽取數字到lottery的set中
    # print(lottery) #check
    # print("長度:",len(lottery)) #check
    paper+=1 #每一次輪迴，都是購買一張彩券

    #TODO(3)從我買的彩券中，一個一個檢視號碼，是否有在官網開出彩券當中
    t=0 #中了幾個號碼
    y=[] #我買的彩券中，哪幾個號碼中獎
    for x in lottery: #從我買的彩券中，一個一個檢視號碼
        if x in award: #如果有在官網開出彩券當中
            y.append(x) #如果我買的彩券中，這個號碼有中獎，則加入y字串中
            t+=1 #並算一次中獎次數

#TODO(5)總結
print("award:",award) #官網開出彩券的號碼
print("lottery:",lottery) #當期我買的彩券號碼
print("中獎的字串:",y)  #哪幾個號碼中獎
print("中了幾個號碼:",t) #中了幾個號碼
print("購買彩券的張數",paper) #購買彩券的張數






