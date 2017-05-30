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
        self.assertEqual(formatLetters("EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"), [
                         'EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR'])
        self.assertEqual(formatLetters("LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"), [
                         'LLARSHAHLC', 'AOOLLAMILL', 'OIDNALHGIH', 'RBAMCETUHS', 'SMOSKAGETR', 'CORCHORROA', 'IDBSLSAAOM', 'IGOSMONDFL', 'HHNGMSDCMA', 'CMIRRSMLHP'])

    def test_makeRows(self):
        self.assertEqual(makeRows(['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']), [
                        'WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'])
        self.assertEqual(makeRows(['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']),
                        ['EZAACBEABB', 'OERANOEBOO', 'ABRCANRCIA', 'RRABBITEOA', 'BACRORCRRK', 'RECRZBBIOR', 'NBOCOBRCRK', 'IROHBNARCE', 'ABNEKCIHCA', 'BHRCAAAROR'])
        self.assertEqual(makeRows(['LLARSHAHLC', 'AOOLLAMILL', 'OIDNALHGIH', 'RBAMCETUHS', 'SMOSKAGETR', 'CORCHORROA', 'IDBSLSAAOM', 'IGOSMONDFL', 'HHNGMSDCMA', 'CMIRRSMLHP']),
                        ['LAORSCIIHC', 'LOIBMODGHM', 'AODAORBONI', 'RLNMSCSSGR', 'SLACKHLMMR', 'HALEAOSOSS', 'AMHTGRANDM', 'HIGUERADCL', 'LLIHTOOFMH', 'CLHSRAMLAP'])

    def test_checkLetters(self):
        self.assertEqual(checkLetters(['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'],
                        ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST'],
                        1,
                        0,
                        [[],[]]),
                        [['SLO', 'UNIX'],  [{'word': 'SLO', 'row': 7, 'col': 2, 'dir': 1, 'reverse': 0}, {'word': 'UNIX', 'row': 9, 'col': 3, 'dir': 1, 'reverse': 0}]])
        self.assertEqual(checkLetters(['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR'],
                        ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON'],
                        1,
                        0,
                        [[],[]]),
                        [['ZEBRA', 'RACCOON'], [{'word': 'ZEBRA', 'row': 1, 'col': 0, 'dir': 1, 'reverse': 0}, {'word': 'RACCOON', 'row': 2, 'col': 2, 'dir': 1, 'reverse': 0}]])
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
        self.assertEqual(checkLetters(['LAORSCIIHC', 'LOIBMODGHM', 'AODAORBONI', 'RLNMSCSSGR', 'SLACKHLMMR', 'HALEAOSOSS', 'AMHTGRANDM', 'HIGUERADCL', 'LLIHTOOFMH', 'CLHSRAMLAP'],
                        ['SLACK', 'HIGH', 'HIGHLAND', 'CHORRO', 'PEACH', 'BROAD', 'GRAND', 'OSOS', 'MORRO', 'HIGUERA', 'MARSH', 'FOOTHILL', 'NIPOMO', 'MILL', 'PALM'],
                        2,
                        0,
                        [[],[]]),
                        [['SLACK', 'OSOS', 'GRAND', 'HIGUERA'], [ {'word': 'SLACK', 'row': 0, 'col': 4, 'dir': 2, 'reverse': 0}, {'word': 'OSOS', 'row': 5, 'col': 5, 'dir': 2, 'reverse': 0},
                        {'word': 'GRAND', 'row': 4, 'col': 6, 'dir': 2, 'reverse': 0}, {'word': 'HIGUERA', 'row': 0, 'col': 7, 'dir': 2, 'reverse': 0}]])
        self.assertEqual(checkLetters(['WCALPOLYXU', 'ABZDOEGCVU', 'QMXWNDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'],
                        ['XNIU', 'YLOPLAC', 'CCG', 'OLS', 'ELIPMOC', 'MIV', 'TSET'],
                        2,
                        1,
                        [[],[]]),
                        [['COMPILE'], [{'word': 'COMPILE', 'row': 6, 'col': 8, 'dir': 2, 'reverse': 1}]])

    def test_reverseWords(self):
        self.assertEqual(reverseWords(['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST']), [
                        'XINU', 'YLOPLAC', 'CCG', 'OLS', 'ELIPMOC', 'MIV', 'TSET'])
        self.assertEqual(reverseWords(['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON']),
                        ['NEKCIHC', 'GOD', 'TAC', 'RAEB', 'TIBBAR', 'ARBEZ', 'ESUOM', 'NOOCCAR'])
        self.assertEqual(reverseWords(['SLACK', 'HIGH', 'HIGHLAND', 'CHORRO', 'PEACH', 'BROAD', 'GRAND', 'OSOS', 'MORRO', 'HIGUERA', 'MARSH', 'FOOTHILL', 'NIPOMO', 'MILL', 'PALM']),
                        ['KCALS', 'HGIH', 'DNALHGIH', 'ORROHC', 'HCAEP', 'DAORB', 'DNARG', 'SOSO', 'ORROM', 'AREUGIH', 'HSRAM', 'LLIHTOOF', 'OMOPIN', 'LLIM', 'MLAP'])

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
