a = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

key1 = input("Enter the Key : ")
k = [['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0']]
l = 0
key = []
for i in key1:
    if i not in key:
        key.append(i)

for i in a:
    if i not in key:
        key.append(i)
        
for i in range(0,5):
    for j in range(0,5):
        if l < len(key):
            k[i][j] = key[l]
            l = l + 1
print(k)
p = input("Enter the Plain Text : ")

o = []
h = 88
for i in p:
    o.append(i)
i = 0
l = len(o)
while i < len(o)-1:
    if o[i] == o[i+1] and i%2 == 0:
        o.insert(i+1,chr(h))
        h = h + 1
        break
    i = i + 1
p = ""
for i in o:
    p = p+i
    
if len(p)%2 != 0:
    p = p + 'X'
pairs = [p[i:i+2] for i in range(0,len(p),2)]
print(pairs)
c = ""
for pair in pairs:
    # Get the row and column indices of each letter in the pair
    positions = []
    for m in pair:
        for e, row in enumerate(k):
            for j, col in enumerate(row):
                if col == m:
                    positions.append((e, j))
    print(positions)

    if positions[0][0] == positions[1][0]:
        print(positions[0][0],",",positions[1][0])
        # Shift to the right (circular) within the same row
        c += k[positions[0][0]][(positions[0][1] + 1) % 5]
        c += k[positions[1][0]][(positions[1][1] + 1) % 5]

    # Check if the letters are in the same column
    elif positions[0][1] == positions[1][1]:
        # Shift down (circular) within the same column
        c += k[(positions[0][0] + 1) % 5][positions[0][1]]
        c += k[(positions[1][0] + 1) % 5][positions[1][1]]

    # Otherwise, they form a rectangle in the matrix
    else:
        # Swap the columns of the two letters
        c += k[positions[0][0]][positions[1][1]]
        c += k[positions[1][0]][positions[0][1]]

print("Encrypted Text:", c)
        

        


