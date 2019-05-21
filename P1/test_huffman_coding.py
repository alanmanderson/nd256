import unittest
import huffman_coding as hc

class TestHuffmanEncoding(unittest.TestCase):

    def test_empty_string(self):
        pass

    def test_character_frequencies(self):
        test_string = 'Hydrogen-monoxide: H2O'
        expects = {
            'H': 2, 'y':1, 'd': 2, 'r':1, 'o':3,
            'g': 1, 'e':2, 'n': 2, '-':1, 'm':1,
            'x': 1, 'i':1, ':':1, ' ':1, '2':1,
            'O':1
        }
        assert expects == hc.get_character_frequencies(test_string)

    def test_character_frequencies_empty_string(self):
        test_string = ""
        expects = {}
        assert expects == hc.get_character_frequencies(test_string)

    def test_get_ordered_tuples(self):
        test_map = {"a": 1, "l": 2, "!": 1}
        expects = [("l", 2), ("a", 1), ("!", 1)]
        assert expects == hc.get_ordered_tuples(test_map)

    def test_get_ordered_tuples_empty_array(self):
        test_map = {}
        expects = []
        assert expects == hc.get_ordered_tuples(test_map)

class TestHuffmanDecoding(unittest.TestCase):

    def test_empty_string(self):
        pass

if __name__ == '__main__':
    unittest.main()
