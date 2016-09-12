# -*- coding: utf-8 -*-
import sys
import jieba

def segWord(rawStr, cutMode = 'fine'):
    if cutMode == 'all':
        segList = jieba.cut(rawStr, cut_all = True)
    elif cutMode == 'fine':
        segList = jieba.cut(rawStr, cut_all = False)
    elif cutMode == 'search':
        segList = jieba.cut_for_search(rawStr)
    return segList

def countWord(segList, freq = dict()):
    # freq = dict()
    passWords = (u'，', u'。', u'、', u'的', u'和', u'在', u'了', u'是') # add 'u' for preventing UnicodeError
    for word in segList:
        # print word
        if word not in passWords:
            freq[word] = freq.get(word, 0) + 1
    # return freq

def main():
    rawFile = sys.argv[1]
    cutMode = sys.argv[2]
    topNo = int(sys.argv[3])
    with open(rawFile, 'r') as f:
        wordFreq = dict()
        for line in f.readlines():
            line = line.strip()
            segLine = segWord(line, cutMode)
            countWord(segLine, wordFreq)
        sortedByValue = sorted(wordFreq, key = wordFreq.get, reverse = True)
        for i in range(topNo):
            word = sortedByValue[i]
            print word, wordFreq[word]

main()

'''
test = '有5个包裹，你明天最好带个大袋子，就放在饮水机旁边的桌子上。'
tmp = segWord(test)
print '/'.join(tmp)
tmpFreq = countWord(tmp)

for word, freq in tmpFreq.items():
    print word, freq
'''
