import re
import sys
from task2 import decrypt
from task3 import getKey


def getIOC(split):
    freqSum = 0
    for i in range(26):
        ni = split.count(chr(i+65))
        freqSum = freqSum + (ni * (ni-1))
    n = float(len(split))
    if n < 2:
        return -1
    ioc = freqSum / (n * (n-1))
    return ioc


def getKeyLen(ciphertext):
    ciphertext = ciphertext.upper()
    ciphertext = re.sub('[^A-Za-z]', '', ciphertext)
    maxLen = 100
    if len(ciphertext) < 100:
        maxLen = len(ciphertext)
    iocTable = []
    for keyLen in range(maxLen+1):
        if keyLen == 0:
            continue
        sumIOC = 0.0
        retIOC = 0.0
        for i in range(keyLen):
            split = ""
            for j in range(0, len(ciphertext), keyLen):
                if (i+j) < len(ciphertext):
                    split = split + ciphertext[i+j]
            retIOC = getIOC(split)
            if retIOC == -1:
                break
            sumIOC = sumIOC + retIOC
        if retIOC == -1:
            break
        avgIOC = sumIOC / keyLen
        iocTable.append(avgIOC)

    smallestDiff = sys.maxsize
    bestLen = 0
    for i in range(len(iocTable)):
        diff = abs(iocTable[i] - 0.0667)
        if diff < smallestDiff:
            bestLen = i + 1
            smallestDiff = diff
        if 0.0727 > iocTable[i] > 0.0607:
            return i + 1
    return bestLen


if __name__ == '__main__':
    text = input()

    keyLength = getKeyLen(text)
    key = getKey(text, keyLength)
    print(key)
    print(decrypt(text, key))
