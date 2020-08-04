#物件→複雜資料
#導向→(1.)結構化、(2.)快速創造資料、(3.)以Excel填表來想像
#Step:(1.)創造設計圖;(2.)藉由設計圖創造資料

# def bmi(height,weight):
#     return weight/((height/100)**2)
#
# class Person: #欄位
#     Name=None
#     weight=None
#     height=None
#
#     def BMI(self): #(自我)專屬技能
#         return self.weight / ((self.height / 100) ** 2)
#
# human1=Person() #藉由設計圖創造資料
# human1.Name="Acer"
# human1.weight=60
# human1.height=160
# bmi(height=human1.height,weight=human1.weight) #呼叫函數(bmi)
# print(human1.Name,bmi(height=human1.height,weight=human1.weight))
# print(human1.Name,(human1.weight/(human1.height/100)**2))
# print(human1.Name,human1.BMI())
#
# human2=Person() #藉由設計圖創造資料
# human2.Name="Ace"
# human2.weight=75
# human2.height=180
# bmi(height=human2.height,weight=human2.weight) #呼叫函數(bmi)
# print(human2.Name,bmi(height=human2.height,weight=human2.weight))
# print(human2.Name,(human2.weight/(human2.height/100)**2))
# print(human2.Name,human2.BMI())
#
# human3=Person() #藉由設計圖創造資料
# human3.Name="Ping"
# human3.weight=50
# human3.height=160
# bmi(height=human3.height,weight=human3.weight) #呼叫函數(bmi)
# print(human3.Name,bmi(height=human3.height,weight=human3.weight))
# print(human3.Name,(human3.weight/(human3.height/100)**2))
# print(human3.Name,human3.BMI())

#TODO初始化
class Person: #欄位
    def __init__(self,Name,Weight,Height): #強迫設定欄位
        self.Name=Name
        self.weight=Weight
        self.height=Height

    def BMI(self): #(自我)專屬技能
        return self.weight / ((self.height / 100) ** 2)

    def overweight(self):
        if self.weight>70:
            return "Yes"
        else:
            return "NO"

    def taller(self):
        if self.height>170:
            return "Yes"
        elif self.height<170:
            return "NO"

human1=Person("Ace",75,180) #藉由設計圖創造資料
print(human1.Name,human1.BMI())
print("體重判斷",human1.overweight())
print("身高判斷",human1.taller())
print()

human2=Person("Acer",60,160)
print(human2.Name,human2.BMI())
print("體重判斷",human2.overweight())
print("身高判斷",human2.taller())
print()

human3=Person(Height=160,Weight=50,Name="Ping") #藉由設計圖創造資料
print(human3.Name,human3.BMI())
print("體重判斷",human3.overweight())
print("身高判斷",human3.taller())
print()