# ------------------------------ #
import math
import sys
import base64
import quickSort
import writing_file
import huffman
import pickle
# text_file = 'test.png'
text_file = 'demo.txt'
coding_file = 'demo_coding.dat'
decoding_file = 'demo_decoding.txt'


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
def get_file_character(tab,text):
    for x in text.read():
        state = 0
        for y in tab:
            if x == y.character :
                state = 1
                y.frequency = y.frequency + 1
                pass
            pass
        if state == 0:
            tab.append(Node(x,1))
            pass
        pass
    n = len(tab)
    quickSort.quickSort(tab, 0, n-1)
    pass
# ------------------------------ #
tab = []
coding_word = {}
decoding_word = {}
text = open(text_file, "r")
get_file_character(tab,text)
huffman.huffman_coding(tab,coding_word)
coding_text = open(coding_file, "r")
huffman.huffman_decoding(coding_word,decoding_word)
decoding_text = open(decoding_file, "r")


# print(coding_text.read())
# print()
# print(decoding_text.read())
# print()

# writing_file.cmp()
