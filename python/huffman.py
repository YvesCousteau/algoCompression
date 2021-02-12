import quickSort
import writing_file
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
def code(seq,node,coding_word):
    if node.character:
        if not seq:
            coding_word[node.character] = "0"
            pass
        else:
            coding_word[node.character] = seq
            pass
        pass
    else:
        code(seq+"0",node.left,coding_word)
        code(seq+"1",node.right,coding_word)
        pass
    pass
# ------------------------------ #
def codeIterative(seq,node,coding_word):
    stack = []
    stack.append(node)
    seq_bin = []
    seq_bin.append(seq)
    while stack:
        curr_node = stack.pop()
        curr_seq = seq_bin.pop()

        if curr_node.character:
            if not curr_seq:
                coding_word[curr_node.character] = "0"
                pass
            else:
                coding_word[curr_node.character] = curr_seq
                pass
            pass
        else:
            if curr_node.left:
                stack.append(curr_node.left)
                seq_bin.append(curr_seq + '0')
                pass
            if curr_node.right:
                stack.append(curr_node.right)
                seq_bin.append(curr_seq + '1')
                pass
            pass
        pass
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
        quickSort.quickSort(tab, 0, n-1)
        pass
    pass
# ------------------------------ #
def huffman_coding(tab,coding_word):
    creat_tree_huffman_coding(tab)
    # code("",tab[0],coding_word)
    codeIterative("",tab[0],coding_word)
    seq = ''
    f = open(text_file, "r")
    for x in f.read():
        for i in coding_word:
            if x == i:
                seq = seq + coding_word[i]
                pass
            pass
        pass
    writing_file.writing_code_seq(seq)
    pass
# ------------------------------ #
def huffman_decoding(coding_word,decoding_word):
    for i in coding_word:
        decoding_word[coding_word[i]] = i
        pass
    f = open(coding_file, "r")
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
    writing_file.writing_decode_seq(text)
    pass
