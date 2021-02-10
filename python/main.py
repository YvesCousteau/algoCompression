# ------------------------------ #
import math
import sys
import base64
# ------------------------------ #
class Node(object):
    frequency = 0
    left = None
    right = None
    character = None
    code = None
    def __init__(self,character,frequency):
        self.character = character
        self.frequency = frequency
        pass
    def setChildren(self,left,right):
        self.left = left
        self.right = right
        pass
    def setCode(self,code):
        self.code = code
        pass
# ------------------------------ #
def quickSort(tab,first,high):
    if len(tab) == 1:
        return tab
    if first < high:
        pi = partition(tab, first, high)
        quickSort(tab, first, pi-1)
        quickSort(tab, pi+1, high)
# ------------------------------ #
def partition(tab, first, high):
    i = (first-1)
    pivot = tab[high]
    for j in range(first, high):
        if tab[j].frequency <= pivot.frequency:
            i = i+1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[high] = tab[high], tab[i+1]
    return (i+1)
# ------------------------------ #
def code(seq,node):
    if node.character:
        if not seq:
            coding_word[node.character] = "0"
            pass
        else:
            coding_word[node.character] = seq
            pass
        pass
    else:
        code(seq+"0",node.left)
        code(seq+"1",node.right)
        pass
    pass
# ------------------------------ #
def get_file_character(tab):
    f = open("demo.txt", "r")

    for x in f.read():
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
    quickSort(tab, 0, n-1)
    pass
    for j in tab:
        pass
# ------------------------------ #
def creat_tree_huffman_coding(tab):
    while len(tab) > 1:
        left = tab.pop(0)
        right = tab.pop(0)
        node = Node(None,right.frequency+left.frequency)
        node.setChildren(left,right)
        tab.append(node)
        n = len(tab)
        quickSort(tab, 0, n-1)
        pass
    pass
# ------------------------------ #
def huffman_coding(tab,coding_word):
    creat_tree_huffman_coding(tab)
    code("",tab[0])
    seq = ''
    f = open("demo.txt", "r")
    for x in f.read():
        for i in coding_word:
            if x == i:
                seq = seq + coding_word[i]
                pass
            pass
        pass
    writing_code_seq(seq)
    pass
# ------------------------------ #
def huffman_decoding(coding_word,decoding_word):
    for i in coding_word:
        decoding_word[coding_word[i]] = i
        pass
    f = open("demo_coding.dat", "r")
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
    writing_decode_seq(text)
    pass
# ------------------------------ #
def writing_code_seq(seq):
    open('demo_coding.dat', 'w').close()
    f = open("demo_coding.dat", "wb")
    text_bytes = seq.encode('ascii')
    f.write(text_bytes)
# ------------------------------ #
def writing_decode_seq(seq):
    open('demo_decoding.txt', 'w').close()
    f = open("demo_decoding.txt", "a")
    f.write(seq)
    pass
# ------------------------------ #
def cmp():
    f = open("demo.txt", "r")
    temp = ''.join(format(ord(x),'b') for x in f.read())
    open('demo_without_huffman.dat', 'w').close()
    f = open("demo_without_huffman.dat", "wb")
    f.write(temp.encode('ascii'))
    pass
# ------------------------------ #
tab = []
coding_word = {}
decoding_word = {}
get_file_character(tab)
huffman_coding(tab,coding_word)
f = open("demo_coding.dat", "r")
print(f.read())
print()
huffman_decoding(coding_word,decoding_word)
f = open("demo_decoding.txt", "r")
print(f.read())
print()
cmp()
