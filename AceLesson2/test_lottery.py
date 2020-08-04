from random import randint

#TODO(2)官網開出彩券

award=set() #設定一個空set，叫做award
while len(award)<7: #當award的set的長度小於7時，執行迴圈;直到有7個數字加入到award的set中才跳出迴圈
    award.add(randint(1,48)) #從1到48號中隨機抽取數字到award的set中
print(award) #check
# print("長度:",len(award)) #check

#TODO(1)我買的彩券
#開出的號碼不重複、都是號碼、沒有順序性→使用set
lottery=set() #設定一個空set，叫做lottery
while len(lottery)<7: #當lottery的set的長度小於7時，執行迴圈;直到有7個數字加入到lottery的set中才跳出迴圈
    lottery.add(randint(1,48)) #從1到48號中隨機抽取數字到lottery的set中
print(lottery) #check
# print("長度:",len(lottery)) #check

#TODO(3)從我買的彩券中，一個一個檢視號碼，是否有在官網開出彩券當中
t=0
for x in lottery: #一個一個檢視號碼
    if x in award: #如果有在官網開出彩券當中
        print(x,"中了") #則顯示號碼及"中了"
        t+=1
print("中了幾個號碼:",t)





