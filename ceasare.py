a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
k = int(input("Enter the shift key :"))
p = input("Enter the plain text :")
p = p.upper()
c = ''
for i in p:
    e = a.index(i)
    d = (e+k)%26
    c = c+a[d]
print("Cipher Text : "+c)
        
