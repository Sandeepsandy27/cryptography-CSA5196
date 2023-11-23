depth = int(input("Enter the Depth: "))
plaintext = input("Enter the Plain text: ")

rails = ['' for _ in range(depth)]
dir = 1  # 1 for down, -1 for up
row = 0

for char in plaintext:
    rails[row] += char
    row += dir

    # Change direction when reaching the top or bottom rail
    if row == 0 or row == depth - 1:
        dir *= -1

ciphertext = ''.join(rails)
print("Cipher: " + ciphertext)
