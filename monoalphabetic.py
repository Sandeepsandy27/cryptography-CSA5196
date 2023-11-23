a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k = input("Enter the Key : ")
p = input("Enter the Plain text : ")
b = []
c = ''
k = k.upper()
p = p.upper()
for i in k:
    if i not in b:
        b.append(i)
for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)
for i in p:
    e = a.index(i)
    c = c+b[e]
print("Cipher Text : "+c)
