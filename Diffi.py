p = int(input("Enter a prime number : "))
a = int(input("Enter the Primitive root of the number : "))
l = []

for i in range(1,p):
    num = (a**i)%p
    if num in l:
        print("Not Primitive root")
        exit()
    l.append(num)
    
x1 = int(input("Enter the Private key of user A : "))
if x1 > p :
    exit()
y1 = (a**x1)%p

print("Public key of user A : ",y1)
x2 = int(input("Enter the Private key of user B : "))
if x2 > p :
    exit()
y2 = (a**x2)%p

print("Public key of user B : ",y2)
k1 = (y2**x1)%p
k2 = (y1**x2)%p

if k1 == k2:
    print("The Common key generated is : ",k1)
else:
    print("The keys generated are : ",k1," and ", k2)
