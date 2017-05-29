# Project 4 - Word Searcher
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05

# ========================================================
# Import libraries
# ========================================================
import unittest
from funcs import *


class TestCases(unittest.TestCase):
    def test_formatLetters(self):
        self.assertEqual(formatLetters("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), [
                         'WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])
        # self.assertEqual(getNewLetter("O"), "X")

    def test_makeRows(self):
        self.assertEqual(makeRows()
        pass

    def test_checkLetters(self):
        self.assertEqual(checkLetters)
        pass

    def reverseWords(self):
        self.assertEqual(reverseWords)
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
