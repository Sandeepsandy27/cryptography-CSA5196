p = int(input("Enter first Prime Number : "))
q = int(input("Enter second Prime Number : "))
n = p*q
r = (p-1)*(q-1)
e = 0
MAX = 999999
def gcd(i,r):
    g = 0
    for j in range(1,r):
        if i%j == 0 and r%j == 0:
            g = j
    return g

for i in range(2,MAX):
    if gcd(i,r) == 1:
        e = i
        break
d = 0
for i in range(2,MAX):
    if (i*e)%r == 1 :
        d = i
        break

print("Public key : ","{",e,",",n,"}")
print("Public key : ","{",d,",",n,"}")

pt = int(input("Enter the Plain text : "))
c = (pt**e)%n
print("After Encryption : ",c)
m = (c**d)%n
print("After Decryption : ",m)
