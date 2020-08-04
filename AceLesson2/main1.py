# Me=["[0]剪刀","[1]石頭","[2]不"]
# print(Me)
# print(Me[1])
# print(Me[0:2])
# print(Me+["[3]鐵鎚"])
# print(len(Me+["[3]鐵鎚"]))
# Me[2]="[2]布"
# print(Me)

# position=0
# while position<len(Me):
#     print(Me[position])
#     position+=1

# for x in Me:
#     for x in Me:
#         if x!="[2]布":
#             print(x,end="<")
#         else:
#             print(x)

# print(len(Me))

# Me=["[0]剪刀","[1]石頭","[2]不"]
# Me[2]="[2]布"
# Me.insert(2,"[3]鐵鎚")
# print(Me)
# Me.remove("[3]鐵鎚")
# print(Me)
# Me=Me+["[3]鐵鎚"]
# print(Me)
# del Me[3]
# print(Me)


#此時會print=None出來
# Me=Me.insert(2,"鐵鎚")
#此時會顯示'NoneType' object is not subscriptable，亦即None的值是無法指定第幾位文字列印出來
# print(Me[0])

# for t in range(0,5,1):
#         if t ==2:
#             continue
#         print(t,"acer")

# Draft
# import random
# List=["A","B","C","D","E"]
# print(List)
# R=random.randint(0,4)
# print(R)
# del List[R]
# print(List)

#Draft
# List=("ABCDEABCDEABCDE")
# # print(List.split(","))
# # List=List.split(",")
# letter=[]
# for i in List:
#     print(i)
#     letter=letter+[i]
# print(letter)
# for i in List:
#     if i in List:
#         continue
# print(letter.count(i))

# x={"A":150,"B":160,"C":170,"D":180,"E":190}
# for p in x.keys():
#     print(p)

# Acer={1,2,3,4,5}
# print(Acer)
# print(len(Acer))
# Acer.add(5)
# print(Acer)
# print(len(Acer))

# a=1/0

try:
    print(int(1/1))
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("try-except-finally")