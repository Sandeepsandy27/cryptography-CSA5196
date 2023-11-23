import numpy as np
import math

p = input("Enter the Plain Text : ")
MAX = 999999
k =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        k[i][j] = int(input("Enter : "))
while len(p)%3 != 0:
    if len(p)%3 != 0:
        p = p + 'X'
print(p)

pairs = [p[i:i+3] for i in range(0, len(p), 3)]

def multiply(matrix1, matrix2):
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[j] += matrix1[i][j] * matrix2[i]
    return result
print("Plain Text Pairs:", pairs)
c = ""
for pair in pairs:
    mat = [ord(pair[0])-65,ord(pair[1])-65,ord(pair[2])-65]
    result = multiply(k,mat)
    print(result)
    result[0] = (result[0]%26)+65
    result[1] = (result[1]%26)+65
    result[2] = (result[2]%26)+65
    
    c = c + chr(result[0])+chr(result[1])+chr(result[2])
print("CIPHER : "+c)

det = (k[0][0]*((k[1][1]*k[2][2])-(k[1][2]*k[2][1])))-(k[0][1]*((k[1][0]*k[2][2])-(k[2][0]*k[1][2])))+(k[0][2]*((k[1][0]*k[2][1])-(k[2][0]*k[1][1])))
d = det%26
print("Determinant : ",d)

adj_A = [
    [(k[1][1]*k[2][2] - k[1][2]*k[2][1]), -(k[0][1]*k[2][2] - k[0][2]*k[2][1]), (k[0][1]*k[1][2] - k[0][2]*k[1][1])],
    [-(k[1][0]*k[2][2] - k[1][2]*k[2][0]), (k[0][0]*k[2][2] - k[0][2]*k[2][0]), -(k[0][0]*k[1][2] - k[0][2]*k[1][0])],
    [(k[1][0]*k[2][1] - k[1][1]*k[2][0]), -(k[0][0]*k[2][1] - k[0][1]*k[2][0]), (k[0][0]*k[1][1] - k[0][1]*k[1][0])]
]

f = 0
for i in range(1,MAX):
    if (i*d)%26 == 1:
        f = i
        break
print(f)

B = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        B[i][j] = math.floor(((adj_A[i][j])*f)%26)

print(B)

print("AFTER DECRYPTION :\n")

pairs = [c[i:i+3] for i in range(0, len(c), 3)]

def multiply(matrix1, matrix2):
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[j] += matrix1[i][j] * matrix2[i]
    return result
print("Plain Text Pairs:", pairs)
m = ""
for pair in pairs:
    mat = [ord(pair[0])-65,ord(pair[1])-65,ord(pair[2])-65]
    result = multiply(B,mat)
    print(result)
    result[0] = (result[0]%26)+65
    result[1] = (result[1]%26)+65
    result[2] = (result[2]%26)+65
    
    m = m + chr(result[0])+chr(result[1])+chr(result[2])
print("PLAIN TEXT : "+m)


        



