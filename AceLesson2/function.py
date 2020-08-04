#預設值(一旦帶入，所有右邊的參數都要有預設值)
#可以做指定帶入
def add(a,b,c=2,d=3):
    print(((a+b)/c)*d)
    return (((a*b)*c)/d)

print("(1)",add(3,5))
print("(2)",add(a=3,b=5,c=1))
print("(2)",add(a=3,b=5,d=2))
# print(add("Acer","Ace"))

#數字合計-使用list
# sum=0
# for x in [1,2,3,4,5]:
#     sum=sum+x
# print(sum)

# 改成函數
# def sum(*list):
#     sum=0
#     for x in list:
#         sum=sum+x
#     return sum
# print(sum(1,2,3,4,5))

#數字合計-使用range
# sum=0
# for x in range(1,11):
#     sum=sum+x
# print(sum)

#改成函數
# def summary(range):
#     summary = 0
#     for x in range:
#         summary = summary + x
#     return summary
# print(summary(range(1,11)))

