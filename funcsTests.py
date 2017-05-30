# Project 4 – Word Puzzle
#
# Name: Dominic Gaiero and Russell Caletena
# Instructor: S. Einakian
# Section: 05
# https://github.com/dgaiero/cpe101-proj4

#     #                         ######
#  #  #  ####  #####  #####     #     # #    # ###### ###### #      ######
#  #  # #    # #    # #    #    #     # #    #     #      #  #      #
#  #  # #    # #    # #    #    ######  #    #    #      #   #      #####
#  #  # #    # #####  #    #    #       #    #   #      #    #      #
#  #  # #    # #   #  #    #    #       #    #  #      #     #      #
## ##   ####  #    # #####     #        ####  ###### ###### ###### ######

 #######
    #    ######  ####  ##### # #    #  ####
    #    #      #        #   # ##   # #    #
    #    #####   ####    #   # # #  # #
    #    #           #   #   # #  # # #  ###
    #    #      #    #   #   # #   ## #    #
    #    ######  ####    #   # #    #  ####

# ========================================================
# Import libraries
# ========================================================
import unittest
from funcs import *


class TestCases(unittest.TestCase):

    def test_formatLetters(self):
        self.assertEqual(formatLetters("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"), [
                         'WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])

    def test_makeRows(self):
        self.assertEqual(makeRows(['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), [
                        'WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'])

    def test_checkLetters(self):
        self.assertEqual(checkLetters(['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'],
                        ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST'],
                        1,
                        0,
                        [[],[]]),
                        [['SLO', 'UNIX'],  [{'word': 'SLO', 'row': 7, 'col': 2, 'dir': 1, 'reverse': 0}, {'word': 'UNIX', 'row': 9, 'col': 3, 'dir': 1, 'reverse': 0}]])
        self.assertEqual(checkLetters(['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'],
                        ['XNIU', 'YLOPLAC', 'CCG', 'OLS', 'ELIPMOC', 'MIV', 'TSET'],
                        1,
                        1,
                        [[],[]]),
                        [['VIM'], [{'word': 'VIM', 'row': 1, 'col': 4, 'dir': 1, 'reverse': 1}]])
        self.assertEqual(checkLetters(['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'],
                        ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST'],
                        2,
                        0,
                        [[],[]]),
                        [['CALPOLY'], [{'word': 'CALPOLY', 'row': 1, 'col': 0, 'dir': 2, 'reverse': 0}]])
        self.assertEqual(checkLetters(['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'],
                        ['XNIU', 'YLOPLAC', 'CCG', 'OLS', 'ELIPMOC', 'MIV', 'TSET'],
                        2,
                        1,
                        [[],[]]),
                        [['COMPILE'], [{'word': 'COMPILE', 'row': 6, 'col': 8, 'dir': 2, 'reverse': 1}]])

    def test_reverseWords(self):
        self.assertEqual(reverseWords(['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST']), [
                        'XINU', 'YLOPLAC', 'CCG', 'OLS', 'ELIPMOC', 'MIV', 'TSET'])
        
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
