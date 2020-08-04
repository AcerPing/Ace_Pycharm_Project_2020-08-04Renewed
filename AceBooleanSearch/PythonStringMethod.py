# x="昨天下雨了，淋濕了"
# print(x.replace("昨天","今天"))
# print(x)
# x="昨天昨天昨天昨天下雨了，淋濕了"
# print(x.replace("昨天","今天",2))

# y=input("請輸入文字一\n")
# z=input("請輸入文字二\n")
# if y==z:
#     print("文字一模一樣")
# elif y.lower()==z.lower():
#     print("文字內容一樣，但大小寫有異")
# else:
#     print("相異")

y=input("請輸入文字一\n")
z=input("請輸入文字二\n")
if y==z:
    print("文字一模一樣")
elif y.upper()==z.upper():
    print("文字內容一樣，但大小寫有異")
else:
    print("相異")