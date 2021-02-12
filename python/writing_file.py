import pickle
# text_file = 'test.png'
text_file = 'demo.txt'
coding_file = 'demo_coding.dat'
decoding_file = 'demo_decoding.txt'
# ------------------------------ #
def writing_code_seq(seq):
    open(coding_file, 'w').close()
    f = open(coding_file, "wb")
    text_bytes = seq.encode('ascii')
    # pickle.dump(text_bytes,f)
    f.write(text_bytes)
# ------------------------------ #
def writing_code_seq_bit(seq):
    open(coding_file, 'w').close()
    f = open(coding_file, "wb")
    text_bytes = seq.encode('ascii')
    # pickle.dump(text_bytes,f)
    f.write(text_bytes)
# ------------------------------ #
def writing_decode_seq(seq):
    open(decoding_file, 'w').close()
    f = open(decoding_file, "a")
    f.write(seq)
    pass
# ------------------------------ #
def cmp():
    f = open(text_file, "r")
    temp = ''.join(format(ord(x),'b') for x in f.read())
    open('demo_without_huffman.dat', 'w').close()
    f = open("demo_without_huffman.dat", "wb")
    f.write(temp.encode('ascii'))
    pass
