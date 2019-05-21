import sys

def huffman_encoding(data):
    return "", ""

def get_character_frequencies(text):
    frequencies = {}
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def get_ordered_tuples(letter_map):
    key_tuple = [(i, letter_map[i]) for i in letter_map.keys()]
    key_tuple.sort(key=lambda x: (x[1], x[0]), reverse=True)
    return key_tuple

def huffman_decoding(data,tree):
    return ""

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
