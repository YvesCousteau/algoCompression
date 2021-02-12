from numpy.lib.scimath import log2
from operator import itemgetter
import math
import quickSort
# ------------------------------ #
class Node(object):
    frequency = 0
    left = None
    right = None
    character = None
    def __init__(self,character,frequency):
        self.character = character
        self.frequency = frequency
        pass
    def setChildren(self,left,right):
        self.left = left
        self.right = right
        pass
# ------------------------------ #
def code(seq, list,coding_word):
    a = []
    b = []
    temp = 0
    sum = 0
    print(len(list))
    if len(list) <= 1:
        if not seq:
            coding_word[list[0].character] = "0"
            pass
        else:
            coding_word[list[0].character] = seq
            print(seq)
            pass
        pass
    else:
        for i in list:
            sum = sum + i.frequency
            pass
        print(sum)
        for i in list:
            if temp <= sum%2:
                temp = temp + i.frequency
                a.append(i)
                pass
            else:
                temp = temp + i.frequency
                b.append(i)
                pass
            pass

        for i in a:
            print(i.character,i.frequency)
            pass

        code(seq + "0",a,coding_word)
        code(seq + "1",b,coding_word)
    pass
# ------------------------------ #
def shannon_fano_coding(tab,coding_word):
    list = []
    for i in tab:
        list.append(i)
        pass
    code('',list,coding_word)
    print(coding_word)
    for i in coding_word:
        print(i)
        pass
