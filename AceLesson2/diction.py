x={"A":150,"B":160,"C":170}
print(len(x))
print(x)
print(x["A"])
x["D"]="aabb"
print(x)
x["B"]=True
print(x)
x["C"]+=10
print(x["C"])
print(x)
del x["D"]
print(x)

for key in x.keys():
    print(key,x[key])