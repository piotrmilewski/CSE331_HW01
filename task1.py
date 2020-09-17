def encrypt(plaintext, cipherKey):
    cipherKey = cipherKey.upper()
    ciphertext = ""
    keyIndex = 0
    for i in range(len(plaintext)):
        currChar = ord(plaintext[i])
        currCiph = ord(cipherKey[keyIndex]) - 65
        # check if current character is alphabetical
        if 91 > currChar > 64 or 123 > currChar > 96:
            # check if current character is uppercase
            if 91 > currChar > 64:
                upper = True
            else:
                upper = False
            # add cipher
            currChar = currChar + currCiph
            # make sure no overflow or underflow
            if (currChar > 91 and upper) or (currChar > 122 and not upper):
                currChar = currChar - 26
            # add to the printed string
            ciphertext = ciphertext + chr(currChar)
            # increment key index and make sure no overflow
            keyIndex = keyIndex + 1
            if keyIndex == len(cipherKey):
                keyIndex = 0
        # if character is non-alphabetical then skip
        else:
            ciphertext = ciphertext + chr(currChar)
    return ciphertext


if __name__ == '__main__':
    text = input()
    key = input()

    print(encrypt(text, key))
