#數值累加實作
# sum=0
# for x in range(1,11):
#     sum=sum+x
# print(sum)

# 數值累加實作
# x=0
# sum=0
# while x<11:
#     sum=sum+x
#     x=x+1
# print(sum)

#數值累加實作
# time=0
# result=0
# while time<10:
#     result=result+(time+1)
#     time=time+1
# print(result)

#迴圈(奇數)
# times=0
# while times<10:
#     print(2*times+1,"acer")
#     times=times+1

#迴圈(逆數)
# times=0
# while times<10:
#     print(10-times,"acer")
#     times=times+1


# # 費氏數列－連續印出三個
# time=0
# while time<10:
#     if time==0:
#         A1 = 0
#         A2 = 1
#         A3 = A1 + A2
#         print(A1, A2, A3)
#         A1=A2
#         A2=A3
#     elif time==1:
#         A1 = A1
#         A2 = A2
#         A3 = A1 + A2
#         print(A1, A2, A3)
#         A1=A2
#         A2=A3
#     else:
#         A1 = A1
#         A2 = A2
#         A3 = A1 + A2
#         print(A1, A2, A3)
#         A1=A2
#         A2=A3
#     time = time + 1

# 費氏數列－連續印出三個，且用for型式
# for time in range(0,10,1):
#     if time==0:
#         A1 = 0
#         A2 = 1
#         A3 = A1 + A2
#         print(A1, A2, A3)
#         A1=A2
#         A2=A3
#     elif time==1:
#         A1 = A1
#         A2 = A2
#         A3 = A1 + A2
#         print(A1, A2, A3)
#         A1=A2
#         A2=A3
#     else:
#         A1 = A1
#         A2 = A2
#         A3 = A1 + A2
#         print(A1, A2, A3)
#         A1=A2
#         A2=A3

#費氏數列
# time=0
# while time<10:
#     if time==0:
#         A1=0
#         A2=1
#         A3=1
#         print("time=0時;", "A3=", A3)
#     elif time==1:
#         A2=1
#         A3=1
#         A4=2
#         print("time=1時;", "A4=", A4)
#     else:
#         Ans=A3+A4
#         A2=A3
#         A3=A4
#         A4=Ans
#         print("time=",time,"時;","Ans=",Ans)
#     time=time+1

# 費氏數列
# time=0
# while time<5:
#     #先初始化
#     if time==0:
#         A1=0
#         A2=1
#         A3=1
#         print("time=0時;", "A3=", A3)
#     #從time=1開始計算之下
#     elif time==1:
#         #前兩項先不動，第三項做相加
#         A2=A2
#         A3=A3
#         A4=A2+A3
#         #前兩項往後移動一格
#         A2=A3
#         A3=A4
#         print("time=1時;", "A4=", A4)
#     else:
#         # 前兩項先不動，第三項做相加
#         A2=A2
#         A3=A3
#         A4=A2+A3
#         # 前兩項往後移動一格
#         A2=A3
#         A3=A4
#         print(A4)
#     time=time+1

# 費氏數列(省去elif)
# time=0
# while time<5:
#     # 先初始化
#     if time==0:
#         A0=0
#         A1=1
#         A2=A0+A1
#         print("最末項",A2)
#     #從time=1開始計算之下
#     else:
#     # 前兩項先不動，第三項做相加
#         A0=A0
#         A1=A1
#         A2=A2
#         A3=A1+A2
#         print("最末項",A3)
#     # 前兩項往後移動一格
#         A0=A1
#         A1=A2
#         A2=A3
#     time=time+1

# #當加到超過300的時候要停下來，最後被加的數字是多少
# x=1
# sum=0
# while sum<300:
#     sum=sum+x
#     x=x+1
# print("最後被加的數字是",x-2)
# #當加到13的時候，sum會是91
# #當加到14的時候，sum才會是105