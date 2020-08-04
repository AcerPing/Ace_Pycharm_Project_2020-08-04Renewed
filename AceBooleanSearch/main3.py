# me=input("請猜拳:[0]剪刀,[1]石頭,[2]布\n")
# me=int(me)
# import random
# computer=random.randint(0,2)
# transfer=["剪刀","石頭","布"]
# print("你出的拳:",transfer[me])
# print("電腦出的拳:",transfer[computer])

# if me==computer:
#     print("平手")
# elif me>computer==(me-1):
#     print("Winner")
# elif me<computer==(me+1):
#     print("Loser")
# elif me==0:
#     if computer==2:
#         print("Winner")
# else:
#     print("Loser")

me=input("請猜拳:[0]剪刀,[1]石頭,[2]布\n")
me=int(me)
import random
computer=random.randint(0,2)
transfer=["剪刀","石頭","布"]
print("你出的拳:",transfer[me])
print("電腦出的拳:",transfer[computer])

if me==computer:
    print("平手")
elif me==(computer+1)%3:
    print("I Win")
# elif me==computer-1:
#     print("I Lose")
# elif me==0:
#     if computer==2:
#         print("I Win")
else:
    print("Loser")