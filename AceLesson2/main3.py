import codecs
#第一種import寫法
# import jieba
import jieba.analyse
# 第二種import寫法
# from jieba import analyse
# 第三種import寫法
from jieba.analyse import  extract_tags

file=codecs.open("a.txt","rb",encoding="utf-8")
#TODO(2)顯示並讀取檔案
article=file.read()
##TODO(3)關閉檔案
file.close()

# jieba.load_userdict("./mydic.txt")
jieba.add_word("美麗島")
jieba.add_word("陳菊")
jieba.add_word("民進黨")

#["詞1","詞2","詞3"]
sep=" ".join(jieba.cut(article))
print(sep)
print("關鍵字:",extract_tags(article,5))