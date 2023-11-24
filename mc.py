a = []

for i in range (65, 91):
    a.append(chr(i))

print(a)
k = input("enter the shift key: ")
p = input("enter the plain text: ")
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
print("cipher text: "+c)
