print("請猜拳:剪刀,石頭,布")
x=input("第一位請猜拳:")
y=input("第二位請猜拳:")
if x=="剪刀":
    if y=="石頭":
        print("輸")
    if y=="布":
        print("贏")
    if y=="剪刀":
        print("平手")
elif x=="石頭":
    if y=="石頭":
        print("平手")
    if y=="布":
        print("輸")
    if y=="剪刀":
        print("贏")
elif x=="布":
    if y=="石頭":
        print("贏")
    if y=="剪刀":
        print("輸")
    if y=="布":
        print("平手")
else:
    print("None","Bug")




