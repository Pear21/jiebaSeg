# -*- coding: utf-8 -*-
import jieba

def segWord(rawStr, mode=False):
    segList = jieba.cut(rawStr, cut_all=mode)
    return segList

def countWord(segList):
    freq = dict() 
    for word in segList:
        # print word
        freq[word] = freq.get(word, 0) + 1
    return freq

test = '有5个包裹，你明天最好带个大袋子，就放在饮水机旁边的桌子上。'
tmp = segWord(test)
# print '/'.join(tmp)
tmpFreq = countWord(tmp)
for word, freq in tmpFreq.items():
    print word, freq
