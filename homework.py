def num (a):
  l = ord(a)
  return chr(l+5)

def Cear (a):
  l = ord(a)
  return chr(l-5)

a= 'y'
print(num(a))
print(Cear(num(a)))