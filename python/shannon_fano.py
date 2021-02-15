from numpy.lib.scimath import log2
from operator import itemgetter
import math
import writing_file
import quickSort
# text_file = 'demo.txt'
text_file = 'hello_world.txt'
coding_file = 'demo_coding.dat'
decoding_file = 'demo_decoding.txt'
coding_file_shannon_fano = 'demo_shannon_fano_coding.dat'
decoding_file_shannon_fano = 'demo_shannon_fano_decoding.txt'
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
    if len(list) <= 1:
        if not seq:
            coding_word[list[0].character] = "0"
            pass
        else:
            coding_word[list[0].character] = seq
            pass
        pass
    else:
        for i in list:
            sum = sum + i.frequency
            pass
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
    seq = ''
    f = open(text_file, "r")
    for x in f.read():
        for i in coding_word:
            if x == i:
                seq = seq + coding_word[i]
                pass
            pass
        pass
    writing_file.writing_code_seq_shannon_fano(seq)
    pass
# ------------------------------ #
def shannon_fano_decoding(coding_word,decoding_word):
    for i in coding_word:
        decoding_word[coding_word[i]] = i
        pass
    f = open(coding_file_shannon_fano, "r")
    seq = f.read()
    code_character = ''
    size = 0
    text = ''
    for i in seq:
        code_character = code_character + i
        size = size + 1
        for j in decoding_word:
            if code_character == j:
                text = text + decoding_word[j]
                seq = seq[size:]
                code_character = ''
                size = 0
                pass
            pass
        pass
    writing_file.writing_decode_seq_shannon_fano(text)
    pass
