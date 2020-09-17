import sys
import numpy as np
from scipy.stats import chisquare
from task2 import decrypt


def freqAnalysis(arr):
    englishFreq = np.array([8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.095, 6, 6.3,
                            9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074])
    lowestStat = sys.maxsize
    alphaIndex = 0
    for j in range(26):
        ceaserArr = np.roll(arr, -j)
        stat = chisquare(ceaserArr, englishFreq)[0]
        if stat < lowestStat:
            alphaIndex = j
            lowestStat = stat
    return chr(alphaIndex+65)


def getKey(ciphertext, cipherKeyLen):
    ciphertextUpper = ciphertext.upper()
    retKey = ""
    freqArray = np.array([0] * 26)
    currKeyIndex = 0
    while currKeyIndex < cipherKeyLen:
        i = 0
        keyIndex = 0
        length = 0
        while i < len(ciphertextUpper):
            currChar = ord(ciphertextUpper[i])
            if 91 > currChar > 64:
                if keyIndex == currKeyIndex:
                    currChar = currChar - 65
                    freqArray[currChar] = freqArray[currChar] + 1
                    length = length + 1
                keyIndex = keyIndex + 1
                if keyIndex == cipherKeyLen:
                    keyIndex = 0
            i = i + 1
        freqArray = freqArray / length
        freqArray = freqArray * 100
        retKey = retKey + freqAnalysis(freqArray)
        freqArray.fill(0)
        currKeyIndex = currKeyIndex + 1
    return retKey


if __name__ == '__main__':
    text = input()
    keyLen = int(input())

    key = getKey(text, keyLen)
    print(key)
    print(decrypt(text, key))
