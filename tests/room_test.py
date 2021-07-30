import unittest

from src.guest import *
from src.room import *
from src.song import *

class TestRoom(unittest.TestCase):

        def setUp(self):
            self.room1 = Room("Abba", 10, 50, 1000)
            self.room2 = Room("Christmas", 5, 30, 600)
            self.room3 = Room("Disco", 20, 75, 2000)

        def test_room1_has_genre(self):
            self.assertEqual("Abba", self.room1.genre)