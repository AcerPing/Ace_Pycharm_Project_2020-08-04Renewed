# TODO:讀取檔案二部曲
# TODO(1)開啟檔案
import codecs
with codecs.open("a.txt","rb",encoding="utf-8") as file:
    # TODO(2)顯示並讀取檔案
    file.read()
    print(file.read())

    #Question:為何會顯示不出來?
    #Answer:因為讀到最後一頁後會是空白，所以顯示出來的也會是空白
    #就像讀一本書，讀完後(最後一頁)會是空白，再顯示出來也會是空白

    # article=file.read()
    # print(article)
