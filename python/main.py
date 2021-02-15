# ------------------------------ #
import math
import sys
import base64
import quickSort
import writing_file
import huffman
import shannon_fano
import pickle
# text_file = 'test.png'
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
coding_huffman_word = {}
decoding_huffman_word = {}
text = open(text_file, "r")
get_file_character(tab,text)
huffman.huffman_coding(tab,coding_huffman_word)
coding_huffman_text = open(coding_file, "r")
huffman.huffman_decoding(coding_huffman_word,decoding_huffman_word)
decoding_huffman_text = open(decoding_file, "r")


coding_shannon_fano_word = {}
decoding_shannon_fano_word = {}
text = open(text_file, "r")
get_file_character(tab,text)
shannon_fano.shannon_fano_coding(tab,coding_shannon_fano_word)
coding_shannon_fano_text = open(coding_file_shannon_fano, "r")
shannon_fano.shannon_fano_decoding(coding_shannon_fano_word,decoding_shannon_fano_word)
decoding_shannon_fano_text = open(decoding_file_shannon_fano, "r")

text_p1 = open(text_file, "r")
text_p2 = open(text_file, "r")
coding_huffman_print = coding_huffman_text.read()
decoding_huffman_print = decoding_huffman_text.read()
coding_shannon_fano_print = coding_shannon_fano_text.read()
decoding_shannon_fano_print = decoding_shannon_fano_text.read()
print("Methode Huffman :\n")
print(text_p1.read())
print("<-- coding -->\n")
print(coding_huffman_print)
tmp_huffman = 0
for i in coding_huffman_print:
    tmp_huffman = tmp_huffman + 1
    pass
print("lenght :",tmp_huffman)
print("\n<-- decoding -->\n")
print(decoding_huffman_print)
print("--------------------------\n")
print("Methode Shannon-Fano :\n")
print(text_p2.read())
print("<-- coding -->\n")
print(coding_shannon_fano_print)
tmp_shannon_fano = 0
for i in coding_shannon_fano_print:
    tmp_shannon_fano = tmp_shannon_fano + 1
    pass
print("lenght :",tmp_shannon_fano)
print("\n<-- decoding -->\n")
print(decoding_shannon_fano_print)
print("--------------------------\n")
print("rapport -> huffman / shannon - fano :",tmp_huffman/tmp_shannon_fano)


# writing_file.cmp()
