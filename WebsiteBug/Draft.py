class Draft:
  def __init__(self,A,B,C):
    self.Name=A
    self.Number=B
    self.Email=C

  def all(self):
    return self.Number+";"+self.Name+";"+self.Email

H1=Draft(A="Ace",B="14",C="ace@example")
print(H1.Name)
print(H1.Number)
print(H1.Email)
print(H1.all())




