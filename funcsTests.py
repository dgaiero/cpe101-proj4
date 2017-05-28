# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Dominic Gaiero
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
        pass

    def test_checkLetters(self):
        pass

    def reverseWords(self):
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
