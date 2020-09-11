ciphertext = input()
cipherKey = input().upper()

plaintext = ""
keyIndex = 0
upper = False
for i in range(len(ciphertext)):
    currChar = ord(ciphertext[i])
    currCiph = ord(cipherKey[keyIndex]) - 65
    # check if current character is alphabetical
    if 91 > currChar > 64 or 123 > currChar > 96:
        # check if current character is uppercase
        if 91 > currChar > 64:
            upper = True
        else:
            upper = False
        # add cipher
        currChar = currChar - currCiph
        # make sure no overflow or underflow
        if (currChar < 65 and upper) or (currChar < 97 and not upper):
            currChar = currChar + 26
        # add to the printed string
        plaintext = plaintext + chr(currChar)
        # increment key index and make sure no overflow
        keyIndex = keyIndex + 1
        if keyIndex == len(cipherKey):
            keyIndex = 0
    # if character is non-alphabetical then skip
    else:
        plaintext = plaintext + chr(currChar)

print(plaintext)
