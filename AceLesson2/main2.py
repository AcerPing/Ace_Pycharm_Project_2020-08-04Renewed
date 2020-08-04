#重點
#所有資源放在專案底下
#檔案路徑:相對路徑

# TODO:讀取檔案二部曲
# TODO(1)開啟檔案
# import codecs
# with codecs.open("a.txt","rb",encoding="utf-8") as file:
#     # TODO(2)顯示並讀取檔案
#     article=file.read()
#     # print(file.read()) #為何會顯示不出來??
#     print(article)

'''
# TODO:讀取檔案三部曲
# TODO(1)開啟檔案
file=codecs.open("a.txt","rb",encoding="utf-8")
#TODO(2)顯示並讀取檔案
print(file.read())
##TODO(3)關閉檔案
file.close()
'''

import codecs
with codecs.open("a.txt","rb",encoding="utf-8") as file:
    article=file.read()
    # print(article)

#TODO:計算文字出現過的次數
#一開始先令x字典中沒有任何的keys及values
x={}
#TODO(1)將單字一個一個抓取出來
for letter in article:
    # print(letter)
    #並計入x字典當中 ("出現過的文字": 出現過的次數)
    #如果抓取出來的這個單字，尚未在x字典當中出現過，則令出現過的次數為1
    if letter not in x.keys():
        x[letter] = 1
    #若有在x字典當中出現過，則出現過的次數+1
    else:
        x[letter]+=1

#最後再將字典顯示出來
# print(x)


#TODO:jieba
import jieba.analyse
keywords=jieba.analyse.extract_tags(article,10)
print("關鍵字:",keywords)



