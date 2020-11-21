import unittest

from tournament import Tournament
from player import Player

class GameTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Player('Nikos', 'rock')
        self.p2 = Player('Tom', 'paper')

        self.p3 = Player('John', 'paper')
        self.p4 = Player('Jack', 'scissors')

        self.p5 = Player('Anna', 'scissors')
        self.p6 = Player('Maria', 'scissors')

        self.p7 = Player('Jo', 'rock')
        self.p8 = Player('Umberto', 'scissors')

    def testPaperWinsRock(self):
        self.assertEqual(self.p2, Tournament().game(self.p1, self.p2, 'hh'))
    
    def testRockWinsScissors(self):
        self.assertEqual(self.p7, Tournament().game(self.p7, self.p8, 'hh'))

    def testDraw(self):
        self.assertEqual(None, Tournament().game(self.p5, self.p6, 'hh'))

    def testScissorsWinsPaper(self):
        self.assertEqual(self.p4, Tournament().game(self.p3, self.p4, 'hh'))


    def testPaperWinsRock_reverse(self):
        self.assertEqual(self.p2, Tournament().game(self.p2, self.p1, 'hh'))
    
    def testRockWinsScissors_reverse(self):
        self.assertEqual(self.p7, Tournament().game(self.p8, self.p7, 'hh'))

    def testDraw_reverse(self):
        self.assertEqual(None, Tournament().game(self.p6, self.p5, 'hh'))

    def testScissorsWinsPaper_reverse(self):
        self.assertEqual(self.p4, Tournament().game(self.p3, self.p4, 'hh'))

    def testHistory(self):
        tournament = Tournament()