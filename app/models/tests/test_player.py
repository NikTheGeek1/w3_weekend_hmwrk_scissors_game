import unittest
from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Player('Nikos', 'rock')
        self.p2 = Player('Kostas', 'paper')

    def testName(self):
        self.assertEqual('Nikos', self.p1.name)

    def testChoice(self):
        self.assertEqual('paper', self.p2.choice)