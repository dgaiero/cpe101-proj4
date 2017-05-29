# Project 4 - Word Searcher
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05

# ========================================================
# Import libraries
# ========================================================
import unittest
from funcs3 import *


class TestCases(unittest.TestCase):
    '''
    def test_readFile(self):
        self.assertEqual(readFile("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"),
                        {'puzzleWords': ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST'], 'puzzleLetters': 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'})
        pass
    '''

    def test_formatLetters(self):
        self.assertEqual(formatLetters("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), [
                         'WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])
        # self.assertEqual(getNewLetter("O"), "X")

    # def test_printBoard(self): "I don't think we need this here because this function does not return a value, but just in case I put it here if we need to test it."
    '''
    def test_makeRows(self):
        self.assertEqual(makeRows("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), [
                        'WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'])
        pass
    '''

    '''
    def test_checkLetters(self):
        self.assertEqual(checkLetters)
        pass
    '''


    def test_reverseWords(self):
        self.assertEqual(reverseWords("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), [
                        'XINU', 'YLOPLAC', 'CCG', 'OLS', 'ELIPMOC', 'MIV', 'TSET'])
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
